"""
User Service Layer
Business logic untuk operasi User
"""
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models.user import User


class UserServiceError(Exception):
    """Custom exception untuk user service"""
    pass


def create_user(username, password, email, nama):
    """
    Membuat user baru
    
    Args:
        username (str): Username
        password (str): Password plain text
        email (str): Email
        nama (str): Nama lengkap
        
    Returns:
        User: Instance user yang baru dibuat
        
    Raises:
        UserServiceError: Jika username atau email sudah digunakan
    """
    try:
        # Cek apakah username sudah ada
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            raise UserServiceError(f"Username '{username}' sudah digunakan")
        
        # Cek apakah email sudah ada
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            raise UserServiceError(f"Email '{email}' sudah digunakan")
        
        # Buat user baru
        user = User(
            username=username,
            email=email,
            nama=nama
        )
        user.set_password(password)
        
        # Simpan ke database
        db.session.add(user)
        db.session.commit()
        
        return user
        
    except IntegrityError as e:
        db.session.rollback()
        raise UserServiceError("Terjadi konflik data (username atau email sudah digunakan)")
    except UserServiceError:
        db.session.rollback()
        raise
    except Exception as e:
        db.session.rollback()
        raise UserServiceError(f"Gagal membuat user: {str(e)}")


def authenticate_user(username, password):
    """
    Autentikasi user berdasarkan username dan password
    
    Args:
        username (str): Username
        password (str): Password plain text
        
    Returns:
        User: Instance user jika autentikasi berhasil, None jika gagal
    """
    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        return user
    
    return None


def get_all_users():
    """
    Mendapatkan semua user
    
    Returns:
        list: List dictionary user (tanpa password)
    """
    users = User.query.all()
    return [user.to_dict() for user in users]


def get_user_by_id(user_id):
    """
    Mendapatkan user berdasarkan ID
    
    Args:
        user_id (int): ID user
        
    Returns:
        User: Instance user atau None jika tidak ditemukan
    """
    return User.query.get(user_id)


def update_user(user_id, username=None, email=None, nama=None):
    """
    Update data user
    
    Args:
        user_id (int): ID user yang akan diupdate
        username (str, optional): Username baru
        email (str, optional): Email baru
        nama (str, optional): Nama baru
        
    Returns:
        User: Instance user yang sudah diupdate
        
    Raises:
        UserServiceError: Jika user tidak ditemukan atau terjadi konflik data
    """
    try:
        user = User.query.get(user_id)
        
        if not user:
            raise UserServiceError(f"User dengan ID {user_id} tidak ditemukan")
        
        # Update username jika diberikan
        if username and username != user.username:
            existing = User.query.filter_by(username=username).first()
            if existing:
                raise UserServiceError(f"Username '{username}' sudah digunakan")
            user.username = username
        
        # Update email jika diberikan
        if email and email != user.email:
            existing = User.query.filter_by(email=email).first()
            if existing:
                raise UserServiceError(f"Email '{email}' sudah digunakan")
            user.email = email
        
        # Update nama jika diberikan
        if nama:
            user.nama = nama
        
        db.session.commit()
        return user
        
    except IntegrityError:
        db.session.rollback()
        raise UserServiceError("Terjadi konflik data (username atau email sudah digunakan)")
    except UserServiceError:
        db.session.rollback()
        raise
    except Exception as e:
        db.session.rollback()
        raise UserServiceError(f"Gagal update user: {str(e)}")


def delete_user(user_id):
    """
    Hapus user berdasarkan ID
    
    Args:
        user_id (int): ID user yang akan dihapus
        
    Returns:
        bool: True jika berhasil dihapus
        
    Raises:
        UserServiceError: Jika user tidak ditemukan
    """
    try:
        user = User.query.get(user_id)
        
        if not user:
            raise UserServiceError(f"User dengan ID {user_id} tidak ditemukan")
        
        db.session.delete(user)
        db.session.commit()
        
        return True
        
    except UserServiceError:
        db.session.rollback()
        raise
    except Exception as e:
        db.session.rollback()
        raise UserServiceError(f"Gagal menghapus user: {str(e)}")