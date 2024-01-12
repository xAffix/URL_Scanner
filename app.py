from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import json

app = Flask(__name__)
app.secret_key = 'Affi@12'  # Change this to a strong secret key
API_KEY = 'AIzaSyDMvM2gNXOnXzDh0d6jXIEW0HeWq8WxzAM'  # Replace with your Google Safe Browsing API key

def check_url_safety(api_key, url):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key=AIzaSyDMvM2gNXOnXzDh0d6jXIEW0HeWq8WxzAM"
    data = {
        "client": {
            "clientId": "your-client-id",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
        {"url": "http://www.urltocheck1.org/"},
        {"url": "http://www.urltocheck2.org/"},
        {"url": "http://www.urltocheck3.com/"}
      ]
        }
    }

    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        threat_matches = json.loads(response.text)
        if threat_matches.get("matches"):
            return "Malicious"
        return "Safe"
    else:
        # Handle API error
        return "Error"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form.get('url')

    if not url:
        flash('Please enter a URL to scan.', 'error')
        return redirect(url_for('index'))

    try:
        result = check_url_safety(API_KEY, url)
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('index'))

    return render_template('result.html', result=result, scanned_url=url)

if __name__ == '__main__':
    app.run(debug=True)
