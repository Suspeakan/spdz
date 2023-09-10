from flask import Flask, render_template, request
import spdzonlytranslit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""

    if request.method == 'POST':
        input_text = request.form['input_text']
        result = spdzonlytranslit.convert_to_cyrillic2(input_text)

    return render_template('index.html', result=result)
