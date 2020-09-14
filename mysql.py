from flask import Flask, jsonify, request, json, render_template
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

local_server = True
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisissecret'
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my.db"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my.db"


db=SQLAlchemy(app)
mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)


class Users(db.Model):
    empid = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.Text)
    emp_date = db.Column(db.Text)
    emp_role = db.Column(db.Text)
    emp_email = db.Column(db.Text, unique=True)
    emp_password = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/users/register', methods=['POST'])
def register():
    emp_name = request.get_json(force=True)['emp_name']
    emp_date = request.get_json(force=True)['emp_date']
    emp_role = request.get_json(force=True)['emp_role']
    emp_email = request.get_json(force=True)['emp_email']
    emp_password = bcrypt.generate_password_hash(request.get_json(force=True)['emp_password']).decode('utf-8')
    created = datetime.utcnow()
    with sql.connect("my.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (emp_name, emp_date, emp_role, emp_email, emp_password, created) VALUES('" + 
        str(emp_name) + "','" +
        str(emp_date) + "','" +
        str(emp_role) + "','" +
        str(emp_email) + "','" +
        str(emp_password) + "','" +
        str(created) + "')")

        con.commit()

        result = {
            'emp_name' : emp_name,
            'emp_date' : emp_date,
            'emp_role' : emp_role,
            'emp_email': emp_email,
            'emp_password' : emp_password,
            'created' : created
        }
 
        return jsonify({'result' : result })


@app.route('/users/login', methods=['POST'])
def login():
    emp_email = request.get_json(force=True)['emp_email']
    emp_password = request.get_json(force=True)['emp_password']

    result = ""

    with sql.connect("my.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users where emp_email = '" +str(emp_email)+"' ")
        rv = cur.fetchone()

        if bcrypt.check_password_hash(rv[5], emp_password):
            access_token = create_access_token(identity = {'emp_name': rv[1], 'emp_date': rv[2], 'emp_role': rv[3], 'emp_email': rv[4]})
            result = access_token
        return result


@app.route('/users/getreport', methods=['POST'])
def getreport():
    start_date = request.get_json(force=True)['start_date']
    end_date = request.get_json(force=True)['end_date']

    with sql.connect("my.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE emp_date BETWEEN '"+str(start_date)+"' AND '"+str(end_date)+"' ")
        rv = cur.fetchall()
    return jsonify(rv)


@app.route('/users/empdetail/<empid>', methods=['POST'])
def empdetail(empid):
    result = ""

    with sql.connect("my.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users where empid = '" +str(empid)+"' ")
        rv = cur.fetchone()
        access_token = create_access_token(identity = {'emp_name': rv[1], 'emp_date': rv[2], 'emp_role': rv[3], 'emp_email': rv[4]})
        result = access_token
        return result


@app.route("/users/emplist", methods=['GET'])
def emplist():
    with sql.connect("my.db") as con:
        cur = con.cursor()    
        con.row_factory = sql.Row

        cur.execute("select * from users")
        rv = cur.fetchall()
        res=[]

        for r in rv:
            result={
                'empid': r[0],
                'emp_name': r[1],
                'emp_date': r[2],
                'emp_role': r[3],
                'emp_email': r[4],
                'emp_password': r[5],
            }
            res.append(result)
    return jsonify(res)


@app.route("/users/barchart", methods=['GET'])
def barchart():
    with sql.connect("my.db") as con:
        cur = con.cursor()    
        con.row_factory = sql.Row
        cur.execute("select count(*) from users")
        rv=cur.fetchone()
        cur.execute("select max(empid) from users")
        rv1=cur.fetchone()
        leave = rv1[0]-rv[0]
        re = [rv1[0], rv[0], leave]
        res= []
        for i in re:
            result={
                'value': i,
            }      
            res.append(result)  
    H= 'HR'
    U= 'User'
    with sql.connect("my.db") as con:
        cur = con.cursor()    
        con.row_factory = sql.Row
        cur.execute("select count(*) from users where emp_role = '"+str(H)+"' ")
        rv=cur.fetchone()
        cur.execute("select count(*) from users where emp_role = '"+str(U)+"' ")
        rv1=cur.fetchone()
        res1={'HR': rv[0], 'User': rv1[0]}
    return jsonify({"pageViews":res,"pageCategory":res1})

@app.route("/users/piechart", methods=['GET'])
def piechart():
    H= 'HR'
    U= 'User'
    with sql.connect("my.db") as con:
        cur = con.cursor()    
        con.row_factory = sql.Row
        cur.execute("select count(*) from users where emp_role = '"+str(H)+"' ")
        rv=cur.fetchone()
        cur.execute("select count(*) from users where emp_role = '"+str(U)+"' ")
        rv1=cur.fetchone()
        re = [rv1[0], rv[0]]
        res1= []
        for i in re:
            result={
                'value': i,
            }      
            res1.append(result)  
    return jsonify({"pageCategory":res1})


@app.route("/users/table", methods=['GET'])
def table():
    with sql.connect("my.db") as con:
        cur = con.cursor()    
        con.row_factory = sql.Row

        cur.execute("select * from users")
        rv = cur.fetchall()

        return jsonify(rv)


@app.route("/users/emp/<empid>", methods=['GET'])
def emp(empid):
    with sql.connect("my.db") as con:
        cur = con.cursor()    
        con.row_factory = sql.Row
        cur.execute("SELECT * FROM users where empid = '"+str(empid)+"' ")
        rv = cur.fetchone()
    return jsonify(rv)

@app.route("/users/delete/<empid>", methods=['DELETE'])
def delete(empid):
    users = Users.query.get(empid)
    db.session.delete(users)
    db.session.commit()
    
    return jsonify({'res':'data deleted'})


@app.route('/users/update/<empid>', methods=['PUT'])
def update(empid):
    emp_name = request.get_json(force=True)['emp_name']
    emp_date = request.get_json(force=True)['emp_date']
    emp_role = request.get_json(force=True)['emp_role']
    emp_email = request.get_json(force=True)['emp_email']
    with sql.connect("my.db") as con:
        
        qry="UPDATE users SET emp_name= ?, emp_role=?, emp_date=?, emp_email=? where empid=?;"

        try:
            cur = con.cursor()
            cur.execute(qry, (emp_name, emp_role, emp_date, emp_email, empid))
            con.commit()
            res = "updated"        
        except:
            res = "not updated"
            con.rollback
        return jsonify(res)

#cur.execute("UPDATE users SET emp_name= `"+str(emp_name)+"` where empid="+empid)

if __name__ == '__main__':
    app.run(debug=True)

  