from flask import Flask, render_template, request
from calculator import calculate_federal_tax
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        income = float(request.form['income'])
        filing_status = request.form['filing_status']
        tax = calculate_federal_tax(income, filing_status)
        return render_template('result.html', tax=tax)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
