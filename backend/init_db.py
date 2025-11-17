"""
Script untuk inisialisasi database
"""
from app import create_app
from app.extensions import db
from flask_migrate import Migrate, init, migrate, upgrade

app = create_app()

with app.app_context():
    # Inisialisasi migrations folder
    print("Initializing migrations...")
    try:
        init()
        print("✓ Migrations folder created")
    except Exception as e:
        print(f"Migrations folder might already exist: {e}")
    
    # Generate migration
    print("\nGenerating migration...")
    try:
        migrate(message="Initial migration - create users table")
        print("✓ Migration file created")
    except Exception as e:
        print(f"Error generating migration: {e}")
    
    # Apply migration
    print("\nApplying migration...")
    try:
        upgrade()
        print("✓ Database tables created successfully!")
    except Exception as e:
        print(f"Error applying migration: {e}")

print("\n✅ Database initialization complete!")