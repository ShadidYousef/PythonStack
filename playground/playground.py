from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def three_boxes():
    return render_template('index.html')
@app.route('/play/<times>')
def any_num_of_boxes(times):
    return render_template('index2.html', times=int(times))
@app.route('/play/<times>/<color>')
def color_box(times, color):
    return render_template('index3.html',color=color, times=int(times))

if __name__=="__main__":
    app.run(debug=True)