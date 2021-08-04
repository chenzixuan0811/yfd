from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def game():
    return render_template('list.html')
@app.route('/monkey')
def monkey():
    return render_template('monkey.html')
@app.route('/hand')
def hand():
    return render_template('手速大挑战2.0.html')
@app.route('/jieya')
def jieya():
    return render_template('解压.html')
@app.route('/get')
def get():
    return render_template('get.html')
@app.route('/monkey_list')
def monkey_list():
    return render_template('monkey_list.html')
@app.route('/monkey_key')
def monkey_key():
    return render_template('monkeyKey.html')
if __name__ == '__main__':
    app.run(port=5001)
