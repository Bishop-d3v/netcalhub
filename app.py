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

if __name__ == '__main__':
    app.run(debug=True)