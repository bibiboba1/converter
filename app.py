from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Курсы обмена
EXCHANGE_RATES = {
    "default": {"buy": 3.6, "sell": 3.8},
    "above_1000": {"buy": 3.63, "sell": 3.77},
    "above_5000": {"buy": 3.65, "sell": 3.75}
}

def get_exchange_rate(amount_rub):
    # Можно будет заменить на условие с EUR эквивалентом
    if amount_rub > 125000:  # Примерно 5000 EUR
        return EXCHANGE_RATES["above_5000"]
    elif amount_rub > 25000:  # Примерно 1000 EUR
        return EXCHANGE_RATES["above_1000"]
    else:
        return EXCHANGE_RATES["default"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    rub_amount = float(data.get("amount", 0))
    rate = get_exchange_rate(rub_amount)
    czk = round(rub_amount / rate["sell"], 2)
    return jsonify({"czk": czk})

if __name__ == '__main__':
    app.run(debug=True)

