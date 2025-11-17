import re


class ValidationError(Exception):
    """Custom exception untuk validation error"""
    pass


def validate_email(email):
    """
    Validasi format email sederhana
    
    Args:
        email (str): Email yang akan divalidasi
        
    Returns:
        bool: True jika valid
        
    Raises:
        ValidationError: Jika format email tidak valid
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError("Format email tidak valid")
    return True


def validate_register_payload(data):
    """
    Validasi payload untuk registrasi user
    
    Args:
        data (dict): Payload dari request
        
    Raises:
        ValidationError: Jika payload tidak valid
    """
    required_fields = ['username', 'password', 'email', 'nama']
    
    # Cek field yang required
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Field '{field}' wajib diisi")
        
        if not isinstance(data[field], str):
            raise ValidationError(f"Field '{field}' harus berupa string")
        
        if not data[field].strip():
            raise ValidationError(f"Field '{field}' tidak boleh kosong")
    
    # Validasi panjang username
    username = data['username'].strip()
    if len(username) < 3:
        raise ValidationError("Username minimal 3 karakter")
    if len(username) > 50:
        raise ValidationError("Username maksimal 50 karakter")
    
    # Validasi panjang password
    password = data['password']
    if len(password) < 6:
        raise ValidationError("Password minimal 6 karakter")
    
    # Validasi email
    email = data['email'].strip()
    validate_email(email)
    
    # Validasi nama
    nama = data['nama'].strip()
    if len(nama) < 3:
        raise ValidationError("Nama minimal 3 karakter")
    if len(nama) > 100:
        raise ValidationError("Nama maksimal 100 karakter")
    
    return True


def validate_login_payload(data):
    """
    Validasi payload untuk login
    
    Args:
        data (dict): Payload dari request
        
    Raises:
        ValidationError: Jika payload tidak valid
    """
    required_fields = ['username', 'password']
    
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Field '{field}' wajib diisi")
        
        if not isinstance(data[field], str):
            raise ValidationError(f"Field '{field}' harus berupa string")
        
        if not data[field].strip():
            raise ValidationError(f"Field '{field}' tidak boleh kosong")
    
    return True


def validate_update_user_payload(data):
    """
    Validasi payload untuk update user
    
    Args:
        data (dict): Payload dari request
        
    Raises:
        ValidationError: Jika payload tidak valid
    """
    # Minimal harus ada satu field yang akan diupdate
    allowed_fields = ['username', 'email', 'nama']
    
    if not any(field in data for field in allowed_fields):
        raise ValidationError("Minimal harus ada satu field yang akan diupdate (username, email, atau nama)")
    
    # Validasi username jika ada
    if 'username' in data:
        if not isinstance(data['username'], str) or not data['username'].strip():
            raise ValidationError("Username tidak boleh kosong")
        username = data['username'].strip()
        if len(username) < 3:
            raise ValidationError("Username minimal 3 karakter")
        if len(username) > 50:
            raise ValidationError("Username maksimal 50 karakter")
    
    # Validasi email jika ada
    if 'email' in data:
        if not isinstance(data['email'], str) or not data['email'].strip():
            raise ValidationError("Email tidak boleh kosong")
        validate_email(data['email'].strip())
    
    # Validasi nama jika ada
    if 'nama' in data:
        if not isinstance(data['nama'], str) or not data['nama'].strip():
            raise ValidationError("Nama tidak boleh kosong")
        nama = data['nama'].strip()
        if len(nama) < 3:
            raise ValidationError("Nama minimal 3 karakter")
        if len(nama) > 100:
            raise ValidationError("Nama maksimal 100 karakter")
    
    return True