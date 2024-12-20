import mysql.connector
from flask import Flask, render_template, request, redirect, flash, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure this is strong and kept secret

# Database connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Megha@2004",
        database="db1"
    )

@app.route('/comment')
def comment():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM comments5")
    comments = cursor.fetchall()
    print(comments)  # Debugging: Check retrieved comments
    cursor.close()
    conn.close()
    return render_template('comments.html', comments=comments)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    username = request.form['username']
    comment = request.form['comment']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comments5 (username, comment) VALUES (%s, %s)", (username, comment))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('comment'))


@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/k')
def knowmore():
    return render_template('k.html')

@app.route('/lpage', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM dbtable1 WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(sql, values)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        if data:
            session['username'] = username
            return redirect('/dashboard')
        else:
            flash('Invalid username or password', 'error')
            return redirect('/lpage')
    return render_template('internloginpage.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard2.html')
    else:
        return redirect(url_for('index'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/recent')
def recent():
    return render_template('recent.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/acc')
def acc():
    return "Account created successfully!!!"

@app.route('/sign', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        mobile_number = request.form["mobile_number"]
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO dbtable1 (username, password, email, mobile_number) VALUES (%s, %s, %s, %s)"
        values = (username, password, email, mobile_number)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/acc')
    return render_template('signuppage.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "SELECT username, email, mobile_number FROM dbtable1 WHERE username = %s"
        values = (username,)
        cursor.execute(sql, values)
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            return render_template('profile.html', username=user_data[0], email=user_data[1], mobile_number=user_data[2])
        else:
            flash('User details not found', 'error')
            return redirect('/lpage')
    else:
        return redirect('/lpage')



if __name__ == '__main__':
    app.run(debug=True)
