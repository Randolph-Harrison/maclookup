from flask import Flask, request, render_template
from handlers import lookup_mac

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup')
def handle_lookup() -> str:
    mac = request.args['mac']
    site = request.args['site']
    result = lookup_mac(mac, site)
    return render_template('index.html', result=result)

@app.route('/bounce_poe')
def handle_bounce_poe() -> str:
    return render_template('index.html', poe_bounced="POE bounced")

if __name__ == '__main__':
    app.run(debug=True)
