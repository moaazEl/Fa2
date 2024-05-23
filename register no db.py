from flask import Flask
from flask import Flask, flash, redirect, render_template, request, redirect,url_for


app = Flask(__name__)
app.secret_key = "donottellanyone"

@app.route('/')
def home():
     return render_template('home.html')

@app.route('/about')
def about():
    return render_template("about.html" )


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        print("in post register")
        user_name = request.form['user_name']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        if user_name == "Fred":
            flash('Username already taken!')
            return redirect(url_for("register"))
        else:
            flash('Registeration successful')
            return render_template('register.html')
    else:  #in get process
        print("in get register")
        return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
