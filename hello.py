'''
this code reference tutorialpoint 

'''

#-----------------------hello world --------------------------------------
from flask import Flask,redirect, url_for,request,make_response
import json
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'


#----------------------route mode-----------------------------------------
@app.route('/hello')
def routetest():
    print "i have something to say ,please smulate this to build route rule"
    return "i 'm ok"


#-------------dinamically url and variavle rule--------------------------
#--------------It is possible to build a URL dynamically, by adding variable parts to the rule parameter----------------
#-------reference -----https://www.tutorialspoint.com/flask/flask_variable_rules.htm-------------

'''
test method^--^
http://localhost:5000/blog/11 
http://localhost:5000/rev/1.1

'''




@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo




#------------------Flask  URL  Building--------------------------------

'''
The url_for() function is very useful for dynamically building a URL for a specific function. 
The function accepts the name of a function as first argument,
and one or more keyword arguments, each corresponding to the variable part of URL.

url:https://www.tutorialspoint.com/flask/flask_url_building.htm

test method in browser:http://123.206.232.46:50/guest/der

'''


@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))





#---------------Flask http method-------------------------------------

'''
reference:https://www.tutorialspoint.com/flask/flask_http_methods.htm

htpp usual method:
GET
Sends data in unencrypted form to the server. Most common method.
HEAD
Same as GET, but without response body
POST
Used to send HTML form data to server. Data received by POST method is not cached by server.
PUT
Replaces all current representations of the target resource with the uploaded content.
DELETE
Removes all current representations of the target resource given by a URL


reference html login.html
<html>
   <body>
      
      <form action = "http://localhost:5000/login" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "nm" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
      
   </body>
</html>

'''
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
      #you must note it will redirect to success view function
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

#it seems that there will be redictted



#-------------------------Falsk Template and engineer----------------------------
'''
reference :https://www.tutorialspoint.com/flask/flask_templates.htm
It is possible to return the output of a function bound to a certain URL in the form of HTML. 
For instance, in the following script, hello() function will render Hello Wor with <h1> tag attached to it.



'''

@app.route('/testhtml/')
def index():
   return '<html><body><h1>Hello World</h1></body></html>'



'''
we will use jinjia template engineer

tmplate wiill be rendered via python data

'''
from flask import  render_template
@app.route('/ym/<user>')
def helloo(user):
   return render_template('hello.html', name = user)



#------------------------Flask static files-------------------------------------

'''
we use js or css via jinjia templates engine

syntax:
src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
but we should think of that can we use tranditional methosd via method
because i have failed!!!!!!!


dir structure

|----templates----index.html
|----static           
|      |_______hello.js
|----hello.py





index.html

<html>

   <head>
      <script type = "text/javascript" 
         src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
   </head>
   
   <body>
      <input type = "button" onclick = "sayHello()" value = "Say Hello" />
   </body>
   
</html>


hello.js

function sayHello() {
   alert("Hello World")
}

'''
@app.route("/index")
def indexd():
   return render_template("index.html")



#------------------------Request Object------------------------
'''
reference url:https://www.tutorialspoint.com/flask/flask_request_object.htm
The data from a client s web page is sent to the server as a global request object. In order to process the request data, it should be imported from the Flask module.

Important attributes of request object are listed below 

    Form  It is a dictionary object containing key and value pairs of form parameters and their values.

    args  parsed contents of query string which is part of URL after question mark (?).

    Cookies   dictionary object holding Cookie names and values.

    files  data pertaining to uploaded file.

    method  current request method.

'''


#-----------------------Send form data to tmplate--------------

'''
this first student form data was sent to result 

result get table data and return a table

student.html

<html>
   <body>
   
      <form action = "http://localhost:5000/result" method = "POST">
         <p>Name <input type = "text" name = "Name" /></p>
         <p>Physics <input type = "text" name = "Physics" /></p>
         <p>Chemistry <input type = "text" name = "chemistry" /></p>
         <p>Maths <input type ="text" name = "Mathematics" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
      
   </body>
</html>


result.html

<!doctype html>
<html>
   <body>
   
      <table border = 1>
         {% for key, value in result.iteritems() %}
         
            <tr>
               <th> {{ key }} </th>
               <td> {{ value }} </td>
            </tr>
            
         {% endfor %}
      </table>
      
   </body>
</html>


The results() function collects form data present in request.form 
in a dictionary object and sends it for rendering to result.html.



'''



@app.route('/form')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)



#----------------------Flask cookie-----------------------------
'''

A cookie is stored on a client s computer in the form of a text file
. Its purpose is to remember and track data pertaining to a clnt  usage for better visitor experience and site statistics.

A Request object contains a cookie s attribute. It is a dictionary object of
 all the cookie variables and their corresponding values, a client has transmitted.
 In addition to it, a cookie also stores its expiry time, path and domain name of the site.

In Flask, cookies are set on response object. Use make_response() function to 
get response object from return value of a view function. 
After that, use the set_cookie() function of response object to store a cookie.
Reading back a cookie is easy. The get() method of request.cookies attribute is used to read a cookie.

'''

@app.route('/cookie')
def cookie():
    return render_template('cookie.html')


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
   
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
   
    return resp


@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'


'''
there cookie needed to understand more!!!! i want to skip it

'''


#----------------------Flask session----------------------------
'''
https://www.tutorialspoint.com/flask/flask_sessions.htm
reference tutorial have problem such as forgetting import
Unlike a Cookie, Session data is stored on server.
Session is the time interval when a client logs 
into a server and logs out of it.
The data, which is needed to be held across this session,
is stored in a temporary directory on the server.


this logical might be complicated

user do not need login  again repeatly!!!!!!
referen 's html have error!!!!!

'''



from flask import session
from flask import Flask, session, redirect, url_for, escape, request
app.secret_key='this is used to crypt'
@app.route('/showsession')
def showsession():
   if 'username' in session:
    #you must note:sseion you have bee used!!!!!!
      username = session['username']
      return 'Logged in as ' + username + '<br>' +  "<b><a href = 'http://123.206.232.46:50/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = 'http://123.206.232.46:50/logining'></b>" + "click here to log in</b></a>"



@app.route('/logining', methods = ['GET', 'POST'])
def logining():
   if request.method == 'POST':
      #this is setting session
      session['username'] = request.form['username']
      #now .it redirect function
      return redirect(url_for('showsession'))
   return '''
    <form action = "http://123.206.232.46:50/logining" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "username" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   '''



@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('showsession'))



#----------------------Flask redirect & Error---------------------------
'''
https://www.tutorialspoint.com/flask/flask_redirect_and_errors.htm
Flask class has a redirect() function. When called, it returns a response object 
and redirects the user to another target location with specified status code.

login.html
 <form action = "http://123.206.232.46:50/redirectlogin" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "username" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>

Note:directory structure need to add !!!!!!!!!
'''
from flask import Flask, redirect, url_for, render_template, request


@app.route('/testredirect')
def start_index():
   return render_template('login.html')
#note:redirect dunction!!!!!!!!!
@app.route('/redirectlogin',methods = ['POST', 'GET'])
def redirectlogin():
   if request.method == 'POST' and request.form['username'] == 'admin' :
       return redirect(url_for('successshow'))
   return redirect(url_for('start_index'))

@app.route('/successdo')
def successshow():
   return 'a'


#--------------------upload file-----------------------
'''
reference:https://www.tutorialspoint.com/flask/flask_file_uploading.htm

<html>
   <body>
   
      <form action = "http://localhost:5000/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
      
   </body>
</html>






'''



from flask import Flask, render_template, request
from werkzeug import secure_filename

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload22_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


#---------------------FLask mail---------------------
"""
reference :https://www.tutorialspoint.com/flask/flask_mail.htm

from flask import Flask
from flask_mail import Mail, Message

mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yang756260386@gmail.com'
app.config['MAIL_PASSWORD'] = 'w!y@i#s$'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/mail")
def testmail():
   msg = Message('Hello', sender = 'yang756260386@gmail.com', recipients = ['756260386@qq.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

"""

#-------------------------------Sql and database---------------------------------

import sqlite3
#create database
try:
    conn = sqlite3.connect('database.db')
except:
    print "Opened database successfully";
try:
    conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    print "Table created successfully";
    conn.close()
except:
    print ''

#add data to html
@app.route('/enternew')
def new_student():
   return render_template('studentfordb.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         print "this is a bug------------------------------>"            
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msgfordb = "Recdrd successfully added"
            print msgfordb
      except:
         con.rollback()
         msgfordb = "error in insert operation"
         print msgfordb
      finally:
         print msgfordb
         return render_template("resultfordb.html",msg='ilove')
         con.close()




#----------------------python and ajax comunicate----------

@app.route('/signUp')
def signUp():
    return render_template('signup.html')



@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    print user,password
    return json.dumps({'status':'OK','user':user,'pass':password});



#--------------------PYTHON flask and json---------------------
@app.route('/testjson', methods=['GET','POST'])
def signUpUser1():
    #user =  request.form['username'];
    #password = request.form['password'];
    #print user,password
    print "i love jquery"
    print(type(json.dumps({'status':'OK','user':'user','pass':'password'})))
    return json.dumps({'status':'OK','user':'user','pass':'password'});


#--------------------PYTHON flask and json---------------------
@app.route('/testajax', methods=['GET','POST'])
def signUpUser2():
    #user =  request.form['username'];
    #password = request.form['password'];
    #print user,password
    #print "i love jquery"
    return render_template("testajax.html");



#-------------------python test canvas----------------
@app.route('/testcanvas', methods=['GET','POST'])
def testcanvas():
    #user =  request.form['username'];
    #password = request.form['password'];
    #print user,password
    #print "i love jquery"
    return render_template("testcanvas.html");


#-------------------python test canvas----------------
'''
there , iwant to test when page run canvas,
if page send http request to server

'''
@app.route('/testcanvasandajax', methods=['GET','POST'])
def testcanvasandajax():
    #user =  request.form['username'];
    #password = request.form['password'];
    #print user,password
    #print "i love jquery"
    return render_template("testcanvasandajax.html");

#-------------------python test github syn----------------
'''
 i test github windows and linux syn
 https://github.com/oxfordyang2016/flask-help
'''
@app.route('/testgithub', methods=['GET','POST'])
def testgithub():
    return "test github success"













#---------------------Flask deployment--------------------------------
'''
reference:https://www.tutorialspoint.com/flask/flask_deployment.htm

we should ask that when we run a applicaion in a host receiving data and 

return data ,why you need apache server ????

you need to know python and wsgi 's connection

there is opinion that python flask implement wsgi

'''













































if __name__ == '__main__':
   app.run('0.0.0.0',50,debug='True')
