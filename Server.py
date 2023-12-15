from flask import Flask, jsonify, request
app = Flask(__name__)
# Предположим, что у нас есть некоторая база данных с информацией о лекарствах
# Здесь мы просто создадим список с некоторыми данными
medicines = [
    {"id": 1, "name": "Аспирин", "price": 10},
    {"id": 2, "name": "Парацетамол", "price": 15},
    {"id": 3, "name": "Ибупрофен", "price": 20}
]
@app.route('/medicines', methods=['GET'])
def get_medicines():
    return jsonify(medicines)
@app.route('/medicines/<int:medicine_id>', methods=['GET'])
def get_medicine(medicine_id):
    for medicine in medicines:
        if medicine['id'] == medicine_id:
            return jsonify(medicine)
    return jsonify({"error": "Лекарство не найдено"})
@app.route('/medicines', methods=['POST'])
def create_medicine():
    new_medicine = {
        "id": len(medicines) + 1,
        "name": request.json['name'],
        "price": request.json['price']
    }
    medicines.append(new_medicine)
    return jsonify(new_medicine), 201
@app.route('/medicines/<int:medicine_id>', methods=['PUT'])
def update_medicine(medicine_id):
    for medicine in medicines:
        if medicine['id'] == medicine_id:
            medicine['name'] = request.json['name']
            medicine['price'] = request.json['price']
            return jsonify(medicine)
    return jsonify({"error": "Лекарство не найдено"})
@app.route('/medicines/<int:medicine_id>', methods=['DELETE'])
def delete_medicine(medicine_id):
    for medicine in medicines:
        if medicine['id'] == medicine_id:
            medicines.remove(medicine)
            return jsonify({"message": "Лекарство успешно удалено"})
    return jsonify({"error": "Лекарство не найдено"})
if __name__ == '__main__':
    app.run()