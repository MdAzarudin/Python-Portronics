from flask import Flask,render_template,redirect,url_for,request
import sqlite3 as sql
app = Flask(__name__)

list_1 = []

@app.route('/')
def portronics():
    return render_template ("portronics.html")

@app.route('/Speakers')
def Speakers():
    con = sql.connect("user.db")
    cur = con.cursor()
    cur.execute("select count1, count2,count3 from count where id=?", (1,))
    fet = cur.fetchone()
    count1 = fet[0]
    count2 = fet[1]
    count3 = fet[2]
    return render_template ("speakers.html", count1 = count1, count2 = count2,count3 = count3)


@app.route('/operate/<counter>/<operation>', methods=["GET", "POST"])
def operate(counter, operation):
    if request.method == "POST":
        con = sql.connect("user.db")
        cur = con.cursor()
        cur.execute("select count1, count2, count3 from count where id=?", (1,))
        fet = cur.fetchone()
        count1 = fet[0]
        count2 = fet[1]
        count3 = fet[2]

        if counter == '1':
            if operation == 'increment' and count1 >= 0:
                count1 += 1
            elif operation == 'decrement' and count1 > 0:
                count1 -= 1
        elif counter == '2':
            if operation == 'increment' and count2 >= 0:
                count2 += 1
            elif operation == 'decrement' and count2 > 0:
                count2 -= 1
        elif counter == '3':
            if operation == 'increment' and count3 >= 0:
                count3 += 1
            elif operation == 'decrement' and count3 > 0:
                count3 -= 1    

        cur.execute("update count set count1=?, count2=?, count3=? where id=1", (count1, count2,count3))
        con.commit()
        return redirect (url_for('Speakers'))

@app.route('/Powerbanks')
def Powerbanks():
    con = sql.connect("user.db")
    cur = con.cursor()
    cur.execute("select count1, count2,count3 from count where id=?", (2,))
    fet = cur.fetchone()
    count1 = fet[0]
    count2 = fet[1]
    count3 = fet[2]
    return render_template ("power.html", count1 = count1, count2 = count2,count3 = count3)

@app.route('/operat/<counter>/<operation>', methods=["GET", "POST"])
def op(counter, operation):
    if request.method == "POST":
        con = sql.connect("user.db")
        cur = con.cursor()
        cur.execute("select count1, count2, count3 from count where id=?", (3,))
        fet = cur.fetchone()
        count1 = fet[0]
        count2 = fet[1]
        count3 = fet[2]

        if counter == '1':
            if operation == 'increment' and count1 >= 0:
                count1 += 1
            elif operation == 'decrement' and count1 > 0:
                count1 -= 1
        elif counter == '2':
            if operation == 'increment' and count2 >= 0:
                count2 += 1
            elif operation == 'decrement' and count2 > 0:
                count2 -= 1
        elif counter == '3':
            if operation == 'increment' and count3 >= 0:
                count3 += 1
            elif operation == 'decrement' and count3 > 0:
                count3 -= 1    

        cur.execute("update count set count1=?, count2=?, count3=? where id=2", (count1, count2,count3))
        con.commit()
        return redirect (url_for('Powerbanks'))

@app.route('/iphone')
def iphone():
    return render_template ("new.html")

if __name__ == "__main__":
    app.run(debug=True)





