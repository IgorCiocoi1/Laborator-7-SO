from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Pagina HTML cu formularul
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplicație pentru procesarea unui array de numere</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #4CAF50;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        label {
            font-size: 16px;
            color: #333;
        }
        input[type="text"] {
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background-color: #e0f7e0;
            border: 1px solid #4CAF50;
            border-radius: 4px;
            text-align: center;
        }
        .error {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            border-radius: 4px;
            text-align: center;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Aplicație pentru procesarea unui array de numere</h1>

    <form method="POST">
        <label for="numbers">Introduceți un array de numere (ex: [1,2,3]):</label>
        <input type="text" id="numbers" name="numbers" value="{{ numbers }}" required>

        <input type="submit" value="Trimite">
    </form>

    {% if result is not none %}
        <div class="result">
            <h3>Suma array-ului este: {{ result }}</h3>
        </div>
    {% endif %}

    {% if error is not none %}
        <div class="error">
            <h3>{{ error }}</h3>
        </div>
    {% endif %}
</div>

</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    numbers = ""

    if request.method == 'POST':
        numbers = request.form['numbers']

        try:
            # Convertim inputul într-un array de numere
            number_list = eval(numbers)  # Folosim eval pentru a evalua expresia introdusă
            if isinstance(number_list, list) and all(isinstance(i, (int, float)) for i in number_list):
                # Trimitem array-ul pentru procesare
                response = requests.post('http://worker:5001/process', json={'numbers': number_list})
                result = response.json().get('result', 'Eroare la procesarea datelor.')
            else:
                error = "Input invalid. Trebuie să fie un array de numere."
        except Exception as e:
            error = f"Eroare la procesarea inputului: {str(e)}"

    return render_template_string(HTML_TEMPLATE, result=result, error=error, numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
