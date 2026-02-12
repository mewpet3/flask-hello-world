from flask import Flask
app = Flask(__name__)
x = 10
y = 10

@app.route('/')
def hello_world():
    global x
    global y
    
    return str(x) + " " + str(y)


@app.route('/left')
def hello_world():
    global x
    global y
    x-=1
    return str(x) + " " + str(y)
@app.route('/right')
def hello_world():
    global x
    global y
    x+=1
    return str(x) + " " + str(y)
@app.route('/up')
def hello_world():
    global x
    global y
    y-=1
    return str(x) + " " + str(y)
@app.route('/down')
def hello_world():
    global x
    global y
    y+=1
    return str(x) + " " + str(y) + '''\n<a href="{{ url_for('/right') }}">Go</a>'''