from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
CHAT_ID = '6297861735'

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
    response = requests.post(url, data=data)
    print(response.text)

    return redirect(url_for('formulaire'))

if __name__ == '__main__':
    app.run(debug=True, port=8000)
