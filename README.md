Email Encryptor

A simple Flask-based application that encrypts and decrypts email addresses using Fernet encryption. This project helps users protect their real email addresses by converting them into an encrypted format.

🚀 Features

Encrypts email addresses securely using Fernet encryption.

Decrypts encrypted emails back to their original form.

Simple web interface to test encryption and decryption.

Uses Flask for the backend and HTML, JavaScript for the frontend.

📌 Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/email-encryptor.git
cd email-encryptor

2️⃣ Install Dependencies

Make sure you have Python 3.10+ installed, then run:

pip install flask cryptography

3️⃣ Run the Application

python app.py

4️⃣ Open in Browser

Go to http://127.0.0.1:5000 and start encrypting emails!

📜 Usage

🔹 Encrypt an Email

Enter an email in the text box.

Click the "Encrypt" button.

The encrypted email will be displayed.

🔹 Decrypt an Email

Copy the encrypted email.

Paste it into the "Decrypt" field.

Click the "Decrypt" button to reveal the original email.

🛠 Project Structure

email-encryptor/
│── app.py           # Flask application
│── encryptor.py     # Encryption and decryption logic
│── secret.key       # Encryption key (generated automatically)
│── templates/
│   ├── index.html   # Frontend UI
└── README.md        # Documentation

🔐 How Encryption Works

Generates a secure encryption key (stored in secret.key).

Encrypts the email address using Fernet encryption.

Decryption is only possible using the same key, ensuring security.

💡 Future Improvements

✅ Store encrypted emails in a database.
✅ Integrate a secure API for encrypted email verification.
✅ Develop a browser extension for automatic email encryption.

Output: 
![image](https://github.com/user-attachments/assets/018ba05b-c943-4fb1-9e10-617c92edc6fa)
