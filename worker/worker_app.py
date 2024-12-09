from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    numbers = data.get('numbers', [])
    
    # Procesăm datele - în acest caz, calculăm suma array-ului
    if isinstance(numbers, list) and all(isinstance(i, (int, float)) for i in numbers):
        result = sum(numbers)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Input invalid. Trebuie să fie un array de numere.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
