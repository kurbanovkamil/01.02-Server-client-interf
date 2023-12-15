import sqlite3
import requests
def get_apteki():
    response = requests.get("http://localhost:5000/apteki")
    return response.json()
def get_medication(apteka_id):
    response = requests.get(f"http://localhost:5000/apteki/{apteka_id}/medication")
    return response.json()
def create_tables():
    conn = sqlite3.connect("apteka.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS apteka
                 (id INT PRIMARY KEY, name VARCHAR, address VARCHAR, phone VARCHAR)''')
    c.execute('''CREATE TABLE IF NOT EXISTS medication
                 (id INT PRIMARY KEY, name VARCHAR, manufacturer VARCHAR, price DECIMAL, apteka_id INT,
                 FOREIGN KEY (apteka_id) REFERENCES apteka (id))''')
    conn.commit()
    conn.close()
def add_apteka(id, name, address, phone):
    conn = sqlite3.connect("apteka.db")
    c = conn.cursor()
    c.execute("INSERT INTO apteka VALUES (?, ?, ?, ?)", (id, name, address, phone))
    conn.commit()
    conn.close()
def add_medication(id, name, manufacturer, price, apteka_id):
    conn = sqlite3.connect("apteka.db")
    c = conn.cursor()
    c.execute("INSERT INTO medication VALUES (?, ?, ?, ?, ?)", (id, name, manufacturer, price, apteka_id))
    conn.commit()
    conn.close()