from flask import Flask, request, render_template
from lookup import lookup_mac

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def handle_lookup():
    mac = request.form['mac']
    site = request.form['site']
    result = lookup_mac(mac, site)
    return f"<p>Lookup Result: {result}"

if __name__ == '__main__':
    app.run(debug=True)
