"""
Application Factory untuk Flask
"""
from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from app.config import Config
from app.extensions import init_extensions
from app.routes.users import users_bp


def create_app(config_class=Config):
    """
    Factory function untuk membuat dan konfigurasi Flask app
    """
    app = Flask(__name__)
    
    # Load konfigurasi
    app.config.from_object(config_class)
    
    # Inisialisasi extensions
    init_extensions(app)
    
    # Register blueprints
    app.register_blueprint(users_bp, url_prefix='/users')
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'OK', 'message': 'Backend is running'}, 200
    
    # ==========================================
    # GLOBAL ERROR HANDLERS
    # ==========================================
    
    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
        """Handle 400 Bad Request errors (including JSON parsing errors)"""
        return jsonify({
            'error': 'Format request tidak valid. Pastikan JSON Anda well-formed dan semua field required terisi.'
        }), 400
    
    @app.errorhandler(NotFound)
    def handle_not_found(e):
        """Handle 404 Not Found errors"""
        return jsonify({
            'error': 'Endpoint tidak ditemukan'
        }), 404
    
    @app.errorhandler(500)
    def handle_internal_error(e):
        """Handle 500 Internal Server Error"""
        # Log error untuk debugging (jangan tampilkan detail ke user)
        app.logger.error(f"Internal server error: {str(e)}")
        return jsonify({
            'error': 'Terjadi kesalahan pada server. Silakan coba lagi nanti.'
        }), 500
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        """Handle all unexpected errors"""
        # Log error untuk debugging
        app.logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({
            'error': 'Terjadi kesalahan yang tidak terduga. Silakan coba lagi nanti.'
        }), 500
    
    return app