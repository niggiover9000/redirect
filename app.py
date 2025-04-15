from flask import Flask, render_template
from waitress import serve
from os import getenv
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv(dotenv_path='.env')
@app.route('/')
def index():
    text=getenv('TEXT')
    link=getenv('LINK')
    """Start page"""
    return render_template('index.html', text=text, link=link)

if __name__ == '__main__':
    debug_mode = eval(getenv('DEBUG', False))
    print(f"DEBUG MODE: {debug_mode}")
    if debug_mode:
        app.run(host=getenv('HOST', "0.0.0.0"), port=getenv('PORT', 5000))
    else:
        serve(app, host=getenv('HOST', "0.0.0.0"), port=getenv('PORT', 5000))