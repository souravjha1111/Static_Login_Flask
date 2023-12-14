from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Sushil', password='sushil123'))
users.append(User(id=2, username='Raj', password='raj123'))
users.append(User(id=3, username='jay', password='jay123'))


app = Flask(__name__)
app.secret_key = 'sushil123raj123jay123'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        print("before_request g.user",g.user)
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        print("Valid USer[0]",user)
        if '123' == password:
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    print("profile Page g.user",g.user)
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')


if __name__ == "__main__":
    app.run(debug=False)
