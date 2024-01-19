from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3

views = Blueprint('views', __name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@views.route("/")
def home():
    return render_template("homepage.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/portfolio")
def portfolio():
    return "Portfolio Page"  # Temporary placeholder

@views.route("/skills")
def skills():
    return "Skills Page"  # Temporary placeholder

@views.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save to the database
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)',
                    (name, email, message))
        conn.commit()
        conn.close()

        flash('Message sent successfully!', 'success')
        return redirect(url_for('views.home'))

    return render_template("contact.html")

@views.route("/messages")
def messages():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM messages')
    messages = cur.fetchall()
    conn.close()
    return render_template("messages.html", messages=messages)
