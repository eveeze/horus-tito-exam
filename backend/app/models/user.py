
from datetime import datetime
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db


class User(db.Model):
    """
    Model untuk tabel users
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    # UBAH DISINI: password_hash menjadi password
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    nama = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    
    def set_password(self, plain_password):
        """
        Hash password dan simpan ke kolom password
        
        Args:
            plain_password (str): Password dalam plain text
        """
        # UBAH DISINI: self.password_hash menjadi self.password
        self.password = generate_password_hash(plain_password)
    
    def check_password(self, plain_password):
        """
        Verifikasi password
        
        Args:
            plain_password (str): Password yang akan dicek
            
        Returns:
            bool: True jika password cocok, False jika tidak
        """
        # UBAH DISINI: self.password_hash menjadi self.password
        return check_password_hash(self.password, plain_password)
    
    def to_dict(self):
        """
        Convert model instance ke dictionary (tanpa password)
        
        Returns:
            dict: Dictionary berisi data user
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'nama': self.nama,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f'<User {self.username}>'