from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '...'  # masque-le avant en prod
CHAT_ID = '...'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/send', methods=['POST'])
def send():
    nom = request.form.get('nom')
    email = request.form.get('email')
    message = f"📬 Nouveau formulaire reçu :\n👤 Nom : {nom}\n📧 Email : {email}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)
    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
