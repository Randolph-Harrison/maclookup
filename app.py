from flask import Flask, request, render_template
from lookup import lookup_mac

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup')
def handle_lookup():
    mac = request.args['mac']
    site = request.args['site']
    result = lookup_mac(mac, site)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
