from flask import Flask, render_template, request, jsonify
from encryptor import encrypt_email, decrypt_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400
    encrypted_email = encrypt_email(email)
    return jsonify({"encrypted_email": encrypted_email})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    encrypted_email = request.form.get("encrypted_email")
    if not encrypted_email:
        return jsonify({"error": "Encrypted email is required"}), 400
    decrypted_email = decrypt_email(encrypted_email)
    return jsonify({"decrypted_email": decrypted_email})

if __name__ == "__main__":
    app.run(debug=True)
