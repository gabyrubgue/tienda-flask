# Flask backend to serve the single-page storefront
# This is minimal: most logic runs in the frontend (static JS) and uses localStorage.
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

# Static files are served automatically by Flask under /static
if __name__ == '__main__':
    # Run with: python app.py
    app.run(debug=True, host='0.0.0.0', port=5000)
