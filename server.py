from flask import Flask
from flask import render_template
from flask import request
from Board import Board
app = Flask(__name__)
bd = Board()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        bd.toggle_outlet()
        return render_template('index.html')

if __name__ == '__main__':
    bd.start_interrupts()
    try:
        app.run(host='0.0.0.0')
    except KeyboardInterrupt:
        bd.cleanup()
