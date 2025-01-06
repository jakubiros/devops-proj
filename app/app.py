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

visits = 0

@app.route('/visits')
def visit_counter():
    global visits
    visits += 1
    return f"This page has been visited {visits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)