from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        Name = details['name']
        UID = details['uid']
        Company_Name = details['cname']
        Email_ID = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(Name,UID,Company_Name,Email_ID) VALUES (%s, %s)",
                    (Name, UID, Company_Name, Email_ID))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
