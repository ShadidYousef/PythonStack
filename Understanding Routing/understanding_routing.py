from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<anything>')
def anything(anything):
    return f"Hi {anything}"
@app.route('/repeat/<int:number>/<anything>')
def repeat(number, anything):
    arr = []
    for i in range(number):
        arr.append(anything)
    return str(arr)
    
if __name__=="__main__":
    app.run(debug=True)
