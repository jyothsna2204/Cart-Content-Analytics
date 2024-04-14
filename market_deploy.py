import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Load data from CSV file
def load_data():
    data = []
    with open('final.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route('/')
def index():
    data = load_data()
    return render_template('market.html', data=data)


@app.route('/submit', methods=['POST'])
def submit():
    selected_item = request.form['selected_image']
    data = load_data()
    selected_data = next(item for item in data if item['lhs'] == selected_item)
    print(f"The item brought together with {selected_item} is {selected_data['rhs']}")
    return render_template('market_result.html', selected_data=selected_data)

if __name__ == '__main__':
    app.run(debug=True)
