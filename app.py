from flask import Flask
app = Flask(__name__)
x = 50
y = 50
maxX = 100
maxY = 100
minX = 0
minY = 0

#class Player:   

def map():
    global x
    global y
    global maxX
    global maxY
    out = "<br>"
    for i in range(maxY):
        if y == i:
            out += ("O"*x-1)+"@"+("O"*maxX-x)+"<br>"
        else:
            out += "O"*maxX
    return out

def baseHTML():
    return "X - " + str(x) + "<br>Y - " + str(y) + f'''{map()}<br><a href="up">up</a><br><a href="left">left</a><a href="down">down</a><a href="right">right</a>'''

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
    html = baseHTML()
    y-=1
    return html
@app.route('/down')
def down():
    global x
    global y
    html = baseHTML()
    y+=1
    return html