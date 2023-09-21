from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def root():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/action', methods=['POST'])
def reset():
    if 'reset_button' in request.form:
        session.clear()
    elif 'increment_button' in request.form:
        session['counter'] += 1
    elif 'user_add_button' in request.form:
        session['counter'] += int(request.form['user_input'])
    return redirect('/')


if __name__ == ("__main__"):
    app.run(debug=True)