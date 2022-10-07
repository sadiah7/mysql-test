from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'bll6rxbmrx78s6i1xgr2-mysql.services.clever-cloud.com'
app.config['MYSQL_DATABASE_URI'] = 'mysql://unzcpyamk9tfvpfx:ug5QtkyFF113DmviwdcU@bll6rxbmrx78s6i1xgr2-mysql.services.clever-cloud.com:3306/bll6rxbmrx78s6i1xgr2'
app.config['MYSQL_USER'] = 'unzcpyamk9tfvpfx'
app.config['MYSQL_PASSWORD'] = 'ug5QtkyFF113DmviwdcU'
app.config['MYSQL_DB'] = 'bll6rxbmrx78s6i1xgr2'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['firstName']
        lastName = details['lastName']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
#         temp = cur.execute("SELECT * FROM MyUsers")
#         records = temp.fetchall()
#         for i in records:
#             print(i)
        mysql.connection.commit()
        cur.close()
        return 'success'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
