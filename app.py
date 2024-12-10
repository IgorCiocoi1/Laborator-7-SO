from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    numbers = ""

    if request.method == 'POST':
        numbers = request.form['numbers']
        try:
            # Convertim inputul într-un array de numere
            number_list = eval(numbers)
            if isinstance(number_list, list) and all(isinstance(i, (int, float)) for i in number_list):
                # Trimitem array-ul pentru procesare
                response = requests.post('http://worker:5001/process', json={'numbers': number_list})
                result = response.json().get('result', 'Eroare la procesarea datelor.')
            else:
                error = "Input invalid. Trebuie să fie un array de numere."
        except Exception as e:
            error = f"Eroare la procesarea inputului: {str(e)}"

    return render_template('index.html', result=result, error=error, numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
