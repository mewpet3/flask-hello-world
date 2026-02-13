from flask import Flask
app = Flask(__name__)
x = 10
y = 10

def baseHTML():
    return str(x) + " " + str(y) + '''\n<a href="up">up</a>\n<a href="down">down</a>\n<a href="left">left</a>\n<a href="right">right</a>'''

@app.route('/')
def hello_world():
    global x
    global y
    html = baseHTML()
    return html


@app.route('/left')
def left():
    global x
    global y
    html = baseHTML()
    x-=1
    return html
@app.route('/right')
def right():
    global x
    global y
    html = baseHTML()
    x+=1
    return html
@app.route('/up')
def up():
    global x
    global y
    html = ""
    y-=1
    return html
@app.route('/down')
def down():
    global x
    global y
    html = baseHTML()
    y+=1
    return html