from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default_checkerboard():
    return render_template('index.html', length = 8, width = 4)
@app.route('/<y>')
def eight_by_four_checkerboard(y):
    return render_template('index.html', length = int(y), width = 4)
@app.route('/<y>/<x>')
def x_by_y_checkerboard(y,x):
    the_width = int(int(x)/2)
    return render_template('index.html', length = int(y), width = the_width)
if __name__ == "__main__":
    app.run(debug=True)