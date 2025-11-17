from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services import user_service
from app.utils.validators import (
    ValidationError,
    validate_register_payload,
    validate_login_payload,
    validate_update_user_payload
)

users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])
def register():
    """
    POST /users/register
    Endpoint untuk registrasi user baru
    """
    # Error handling spesifik (Validasi & Service) tetap dipertahankan
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body harus berupa JSON'}), 400
        
        # Validasi payload
        validate_register_payload(data)
        
        # Buat user baru
        user_service.create_user(
            username=data['username'].strip(),
            password=data['password'],
            email=data['email'].strip(),
            nama=data['nama'].strip()
        )
        
        return jsonify({'message': 'Registrasi berhasil'}), 201
        
    except ValidationError as e:
        # Menangkap error validasi input (misal: email tidak valid)
        return jsonify({'error': str(e)}), 400
    except user_service.UserServiceError as e:
        # Menangkap error logika bisnis (misal: username sudah terpakai)
        return jsonify({'error': str(e)}), 400
    # Tidak perlu 'except Exception', Global Handler akan menangkap crash tak terduga


@users_bp.route('/login', methods=['POST'])
def login():
    """
    POST /users/login
    Endpoint untuk login dan mendapatkan JWT token
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body harus berupa JSON'}), 400
        
        # Validasi payload
        validate_login_payload(data)
        
        # Autentikasi user
        user = user_service.authenticate_user(
            username=data['username'].strip(),
            password=data['password']
        )
        
        if not user:
            return jsonify({'error': 'Username atau password salah'}), 401
        
        # Generate JWT token
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'message': 'Login berhasil',
            'token': access_token
        }), 200
        
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    # Error lain (database mati, bug kode) otomatis lari ke Global Handler 500


@users_bp.route('', methods=['GET'])
def get_users():
    """
    GET /users
    Endpoint untuk mendapatkan semua user (tanpa password)
    """
    # Perhatikan: Di sini kita bisa MENGHAPUS blok try-except sepenuhnya!
    # Karena function ini tidak melempar ValidationError user,
    # dan jika ada error database, kita ingin Global Handler yang menangani.
    
    users = user_service.get_all_users()
    return jsonify(users), 200


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    PUT /users/<id>
    Endpoint untuk update data user
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body harus berupa JSON'}), 400
        
        # Validasi payload
        validate_update_user_payload(data)
        
        # Update user
        user_service.update_user(
            user_id=user_id,
            username=data.get('username', '').strip() if 'username' in data else None,
            email=data.get('email', '').strip() if 'email' in data else None,
            nama=data.get('nama', '').strip() if 'nama' in data else None
        )
        
        return jsonify({'message': 'Data user berhasil diperbarui'}), 200
        
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    except user_service.UserServiceError as e:
        # Cek apakah error karena user tidak ditemukan
        if 'tidak ditemukan' in str(e):
            return jsonify({'error': str(e)}), 404
        return jsonify({'error': str(e)}), 400


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    DELETE /users/<id>
    Endpoint untuk menghapus user
    """
    try:
        user_service.delete_user(user_id)
        return jsonify({'message': 'User berhasil dihapus'}), 200
        
    except user_service.UserServiceError as e:
        # Cek apakah error karena user tidak ditemukan
        if 'tidak ditemukan' in str(e):
            return jsonify({'error': str(e)}), 404
        return jsonify({'error': str(e)}), 400