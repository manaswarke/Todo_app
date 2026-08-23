from bottle import *
from sqlite3 import *

def db_setup():
        con = None
        try:         
               con = connect("todo.db")
               sql = "create table if not exists todo(id integer primary key autoincrement, task text)"
               cursor = con.cursor()
               cursor.execute(sql)
               con.commit()
               print("done")
        except Exception as e:
               print("issue ", e)
               con.rollback()
        finally:
               if con!= None:
                        con.close()

db_setup()

application = Bottle()

@application.route("/", method=["POST", "GET"])
def home():
         if request.method == "POST":
               task = request.forms.get("task")
               con = None
               try:
                      con = connect("todo.db")
                      sql = "insert into todo(task) values(?)"
                      cursor = con.cursor()
                      cursor.execute(sql, (task,))
                      con.commit()
               except Exception as e:
                      print("issue ",e)
                      con.rollback()
               finally:
                      if con!= None:
                              con.close()
         con = None
         try:
                con = connect("todo.db")
                sql = "select * from todo"
                cursor = con.cursor()
                cursor.execute(sql)
                data = cursor.fetchall() 
         except Exception as e:
                print("issue ", e)
         finally:
                if con != None:
                         con.close()

         return template("home.tpl", msg=data)

@application.route("/delete/<i.int>")
def delete(i):
        con = None
        try:
               con = connect("todo.db")
               sql = "delete from todo where id=?"
               cursor = con.cursor()
               cursor.execute(sql,(i,))
               con.commit()
        except Exception as e:
               print("issue ", e)
               con.rollback()
        finally:
               if con !=None:
                        con.close() 
        redirect("/")

# run(application, host="localhost", port=4050, debug=True, reloader=True)