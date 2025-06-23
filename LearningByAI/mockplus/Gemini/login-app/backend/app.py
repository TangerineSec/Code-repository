# backend/app.py
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from captcha_generator import generate_captcha_image
import io

# Initialize Flask App
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Store the current captcha text server-side
current_captcha_text = ""

@app.route('/api/captcha', methods=['GET'])
def get_captcha():
    """
    Generates and returns a new captcha image.
    """
    global current_captcha_text
    image, text = generate_captcha_image()
    current_captcha_text = text

    print(current_captcha_text)
    
    # Serve the image directly
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/api/login', methods=['POST'])
def login():
    """
    Handles the user login request.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    captcha = data.get('captcha')

    # --- Input Validation ---
    if not all([username, password, captcha]):
        return jsonify({"success": False, "message": "Missing username, password, or captcha"}), 400

    # --- Captcha Validation ---
    # Note: In a real-world scenario, you'd use a more secure session-based approach.
    if captcha.lower() != current_captcha_text.lower():
        return jsonify({"success": False, "message": "Invalid captcha"}), 401

    # --- User Authentication ---
    # This is a mock authentication. Replace with your actual database lookup.
    if username == 'admin' and password == 'password':
        return jsonify({
            "success": True,
            "message": "Login successful!",
            "token": "fake-jwt-token-for-admin" # Return a token on successful login
        })
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401

if __name__ == '__main__':
    # Run the app on port 5001 to avoid conflicts with frontend dev server
    app.run(debug=True, port=5001)
