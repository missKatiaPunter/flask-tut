from flask import Flask, render_template
from flask_frozen import Freezer
import sys

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)



