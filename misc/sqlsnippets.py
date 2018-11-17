#from flask_mysqldb import MySql
#from wtforms import Form,StringField, TextAreaField, PasswordField, validators
#from passlib.hash import sha256_crypt
#from functools import wraps

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER']='root'
#app.config['MYSQL_PASSWORD'] = '123456'
#app.config['MYSQL_DB'] = 'ridemyway'
#app.config['MYSQL_CURSOR'] = 'DictCursor'
#initalize MySql
#mysql = MYSQL(app)
#this are the routes for the whole application/websites
#the routes to access different types of
# areas in the app are all locatedhere

fecth single id from the db : rides page
    #create cursor
    #cur = mysql.connection.cursor()
    #get ride////we are getting a single ride
    #result = cur.execute("SELECT * FROM rides WHERE id = %s", [id])
    #the variable
    #ride = cur.fetchall()
    #return render_template('article.html' article = article)

#user registration class
#class RegisterForm(Form):
    #name = StringField('Name', [validators.Length(min = 1 , max = 50)])
    #username =  StringField('Username', [validators.Length(min = 5 , max = 7)])
    #email = StringField('Email',[validators.Length(min = 6, max = 50)])
    #password = PasswordField('Password',[
            #validators.DataRequired(),
            #validators.EqualTo('confirm', message= 'Password dont match')
    #])
    #confirm = PasswordField('Confirm Password')



sql log in page:

if request.method == 'POST':
    #get form fills
    username = request.form['username']
    password_candidate = request.form['password']

    form = Users.users.append({'username':username,'password':password_candidate})
    #create a cursor
    #cur = mysql.connection.cursor()
    #get user by Username
    #result = cur.execute("SELECT * FROM user WHERE  username = %s", [username])
    #if result >0:
         #get stored hash
         #data = cur.fetchone()
         #password = data['password']
         #COMPARE Password
        #if sha256_crypt.verify(password_candidate, password):
            #everything passes
            #session ['logged_in'] = True
            #session['username']= username
            #flash('You are now logged in', 'success')
            #return redirect(url_for('home.html'))
        #else:
            #error = 'Invalid log in'
            #return render_template('login.html',error)
        #cur.close()
    #else:
        #error = 'Username not found'
        #return render_template('login.html',error = error)
#return render_template('login.html', form = form)




    #return redirect(url_for('home.html'))

#app routes security checking if user is logged in or not
#def is_logged_in(f):
    #@wraps(f)
    #def wrap(*arg, **kwargs):
        #if 'logged_in' in session:
            #return f(*args, **kwargs)
        #else:
            #flash('Unauthorized please log in','danger')
            #return redirect(url_for('login.html'))
    #return wrap

====================================================
    #retrieving all the data  from the db
    #cur mysql.connection.cursor()
    #get articles
    #result = cur.execute("SELECT * FROM rides")
    #a variable that will fetch everything from the db
    #rides = cur.fetchall()
    #if result > 0:#if there are rows in the table greater than one then the ui should render the data
        #return render_template ('home.html', rides = rides)
    #else:
        #msg = 'No rides availbale now'
        #return render_template('home.html' msg=msg)
    #close connection
    #cur.close()
    ==================================================

    #the rides here have been accesed
    #from the data.py file through importation

#Add Ride form class
#class AddFormRide(Form):
    #ride = StringField('ride',[validators.Length(min = 6, max = 50)])
    #ridedescription = StringField('ridedescription',[validators.Length(min = 15)])
========================================================
#form = AddFormRide(request.form)
#if request.method === 'POST' and form.validate():
    #ride = form.ride.data
    #body = form.ridedescription.data
    #create db cursor
    #cur  =  mysql.connection.cursor()
    #execute
    #cur.execute("INSERT INTO rides(ride,body,name) VALUES(%s,%s,%s)",(ride,body,session['username']))
    # commit to db
    #mysql.connection.commit()
    #close connection to mongo db
    #cur.close()
    #flash('article created' 'success')
    #return redirect(url_for('home.html'))

    ========================================================

    #app logout
    #@app.route('/logout')
    #@is_logged_in
    #def logout():
        #session.clear()
        #flash('You are now logged out','sucess')
        #return redirect(url_for('login.html'))

    #app initalize function/ call the app function to start the whole application
=========sign up
#form = RegisterForm(request.form)
#if request.method == 'POST' and form.validate():
    #name = form.name.data
    #email = form.email.data
    #username = form.username.data
    #password = sha256_crypt.encrypt(str(form.password.data))
    #create a cursor
    #cur = mysql.connection.cursor()
    #Executing query
    #cur.execute("INSERT INTO user (name, email, username, password) VALUES(%s,%s,%s,%s)",(name,email,username,password))
    #commit to db (MYSQL)
    #mysql.connection.commit()
    #Close connection
    #cur.close()
    #flash('You are now registered and can log in' , 'success')
    #redirect(url_for('login.html'))
#return render_template('register.html' ,form = Rides)

=======auth security route
#@is_logged_in
