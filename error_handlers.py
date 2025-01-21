# error_handlers.py

from flask import jsonify

# 404 Error handler
def handle_404(error):
    return jsonify({
        "error": error.name,
        "message": error.description or "The requested resource was not found"
    }), 404

# 401 Error handler
def handle_401(error):
    return jsonify({
        "error": "Unauthorized",
        "message": error.description or "Access denied"
    }), 401

# 500 Error handler
def handle_500(error):
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred"
    }), 500