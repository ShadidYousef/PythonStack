from flask import Flask, render_template, request
app = Flask(__name__) 

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_name = request.form['username']
    user_location = request.form['location']
    user_language = request.form['language']
    user_comment = request.form['textarea']
    return render_template('result.html', user_name=user_name, user_location=user_location, user_language=user_language, user_comment=user_comment)

if __name__=="__main__":
    app.run(debug=True) 