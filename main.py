from flask import Flask, request
import requests
import os

app = Flask(__name__)

# System environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    if data:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": data, "parse_mode": "Markdown"}
        requests.post(url, json=payload)
        return "OK", 200
    return "No Data", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
