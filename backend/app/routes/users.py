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
    Endpoint untuk registrasi user baru (Public)
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body harus berupa JSON'}), 400
        
        validate_register_payload(data)
        
        user_service.create_user(
            username=data['username'].strip(),
            password=data['password'],
            email=data['email'].strip(),
            nama=data['nama'].strip()
        )
        
        return jsonify({'message': 'Registrasi berhasil'}), 201
        
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    except user_service.UserServiceError as e:
        return jsonify({'error': str(e)}), 400


@users_bp.route('/login', methods=['POST'])
def login():
    """
    POST /users/login
    Endpoint untuk login dan mendapatkan JWT token (Public)
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body harus berupa JSON'}), 400
        
        validate_login_payload(data)
        
        user = user_service.authenticate_user(
            username=data['username'].strip(),
            password=data['password']
        )
        
        if not user:
            return jsonify({'error': 'Username atau password salah'}), 401
        
       
        access_token = create_access_token(identity=str(user.id))
        
        return jsonify({
            'message': 'Login berhasil',
            'token': access_token
        }), 200
        
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400


@users_bp.route('', methods=['GET'])
@jwt_required()
def get_users():
    """
    GET /users
    Endpoint untuk mendapatkan semua user (Protected)
    """
    users = user_service.get_all_users()
    return jsonify(users), 200


@users_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    """
    GET /users/<id>
    Endpoint untuk mendapatkan detail satu user (Protected)
    """
    user = user_service.get_user_by_id(user_id)
    
    if not user:
        return jsonify({'error': 'User tidak ditemukan'}), 404
        
    return jsonify(user.to_dict()), 200


@users_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    """
    PUT /users/<id>
    Endpoint untuk update data user (Protected)
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body harus berupa JSON'}), 400
        
        validate_update_user_payload(data)
        
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
        if 'tidak ditemukan' in str(e):
            return jsonify({'error': str(e)}), 404
        return jsonify({'error': str(e)}), 400


@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    """
    DELETE /users/<id>
    Endpoint untuk menghapus user (Protected)
    """
    # Logic Mencegah Hapus Diri Sendiri
    current_user_id = get_jwt_identity()
    
    # Konversi ke string agar perbandingan aman 
    if str(current_user_id) == str(user_id):
        return jsonify({
            'error': 'Anda tidak dapat menghapus akun sendiri saat sedang login.'
        }), 403
        
    try:
        user_service.delete_user(user_id)
        return jsonify({'message': 'User berhasil dihapus'}), 200
        
    except user_service.UserServiceError as e:
        if 'tidak ditemukan' in str(e):
            return jsonify({'error': str(e)}), 404
        return jsonify({'error': str(e)}), 400