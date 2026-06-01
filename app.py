from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subnet-calculator')
def subnet_calculator():
    return render_template('subnet.html')

@app.route('/vlsm-calculator')
def vlsm_calculator():
    return render_template('vlsm.html')

@app.route('/acl-generator')
def acl_generator():
    return render_template('acl.html')

@app.route('/wildcard-calculator')
def wildcard_calculator():
    return render_template('wildcard.html')

@app.route('/ip-binary-converter')
def ip_binary_converter():
    return render_template('binary.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy.html')

@app.route('/guides/vlsm')
def guide_vlsm():
    return render_template('guide_vlsm.html')

@app.route('/guides/subnetting')
def guide_subnetting():
    return render_template('guide_subnetting.html')

@app.route('/guides/acl')
def acl_guide():
    return render_template('acl_guide.html')

@app.route('/guides/wildcard')
def wildcard_guide():
    return render_template('wildcard_guide.html')

@app.route('/ads.txt')
def ads_txt():
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)), 'ads.txt')

if __name__ == '__main__':
    app.run(debug=True)