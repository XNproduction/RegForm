import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Настройки SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "xnreserv@gmail.com"  # Замени на свою почту
PASSWORD = "lvwy eacr jubo zcdp"      # Пароль приложения (генерируется в Google)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    try:
        # Формируем данные из формы
        first_name = data.get("first-name")
        last_name = data.get("last-name")
        dob = data.get("dob")
        age = data.get("age")
        gender = data.get("gender")
        email = data.get("email")
        languages = ", ".join(data.get("language", []))

        # Составляем сообщение
        message = f"""
        New Registration Submitted:
        First Name: {first_name}
        Last Name: {last_name}
        Date of Birth: {dob}
        Age: {age}
        Gender: {gender}
        Email: {email}
        Programming Languages: {languages}
        """
        msg = MIMEText(message)
        msg["Subject"] = "New Registration"
        msg["From"] = EMAIL
        msg["To"] = "xnreserv@gmail.com"

        # Отправка письма
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, "xnreserv@gmail.com", msg.as_string())

        return jsonify({"status": "success", "message": "Form submitted successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
