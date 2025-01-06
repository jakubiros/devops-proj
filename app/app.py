from flask import Flask

app = Flask(__name__)
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello, %s!' % name

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return "This is About page."

@app.route('/time')
def server_time():
    now = datetime.now()
    return f"Current server time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)