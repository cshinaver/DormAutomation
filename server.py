from flask import Flask
from flask import render_template
from flask import request
from Board import Board
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return "post request"

if __name__ == '__main__':
    bd = Board()
    bd.start_interrupts()
    app.run()
