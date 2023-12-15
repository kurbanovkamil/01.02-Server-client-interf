from flask import Flask, render_template, request
import requests
from database import get_apteki, get_medication
app = Flask(__name__)
def get_apteki():
    response = requests.get("http://localhost:5000/apteki")
    return response.json()
def get_medication(apteka_id):
    response = requests.get(f"http://localhost:5000/apteki/{apteka_id}/medication")
    return response.json()
@app.route('/')
def index():
    apteki = get_apteki()
    return render_template('index.html', apteki=apteki)
@app.route('/apteka/<int:apteka_id>')
def apteka(apteka_id):
    apteki = get_apteki()
    apteka = next((apteka for apteka in apteki if apteka['id'] == apteka_id), None)
    if apteka:
        medication = get_medication(apteka_id)
        return render_template('apteka.html', apteki=apteki, apteka=apteka, medication=medication)
    else:
        return "Аптека не найдена"
if __name__ == '__main__':
    app.run()
