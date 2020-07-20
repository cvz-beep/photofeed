from flask import Flask, render_template
import sqlite3

# In this project, I create two flexboxes, placed horizontally. In one, there is an option to upload the
# photo, and in the other there is a static newsfeed. I use flask, python, html and JS.
app = Flask(__name__)


conn = sqlite3.connect('database.db')
print("initialised database successfully")

conn.execute('CREATE TABLE user (username TEXT, password TEXT')
print("Table created successfully")
conn.close()

@app.route('/index')
def index():
    return render_template("index.html")

def photo_display_unit(select ):
    name =
    return render_template("index.html")

@app.route('/register_and_login')
def reg_and_login():
    return render_template("register_and_login.html")


@app.route('/upload_and_feed')
def upload_and_feed_page():
    return render_template("upload_and_photofeed.html")


if __name__ == '__main__':
    app.run()
