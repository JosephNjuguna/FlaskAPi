"""the fisrt time am not supposed to use db = mysql



the first time am supposed to use MySql  :
here are the procedures that am supposed to users

#sudo apt-get install mysql-server libmysqlclient-dev



to start msql server::


mysql -u root -p


after that:


SHOW DATABASES


CREATE A NEW DATABASE ridemyway

USE ridemyway

create user table

CREATE TABLE users(
id INT(11) AUTO_INCREMENT PRIMARY KEY ,
name VARCHAR(100),
email VARCHAR(100),
username VARCHAR(30),
password VARCHAR(100),
register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ):

SHOW TABLES;

DESCRIBE users;

"





what to install when using flask

pip install flask-mysqldb

#FOR FORM VALIDATION :::::
pip Flask-WTF

#HASHING THE USER AUTH PASSWORD
pip install passlib





first things to import in flask:::


Flask
render_template
flash(messages: error, success,alert)
redirect (handles redirect of links)
url_for(redirect to certain templates)
session
logging


(


STORING RIDES IN THE DB


CREATE TABLE rides (id INT(11) AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255), driver VARCHAR(100),
body TEXT ,
create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);


ADD A RIDE ====
<!--{%  from "includes/_formhelpers.html" import render_field %}-->
<!--{{ render_field(form.ride, class_=form-control) }}-->
<!--{{ render_field(form.body, class_="form-control") }}-->


USER REGISTRATION Form

    <!--{{render_field(form.name, class_="form-control")}}-->
    <!--{{render_field(form.email, class_="form-control")}}-->
    <!--{{render_field(form.username, class_="form-control")}}-->
    <!--{{render_field(form.password, class_="form-control")}}-->
    <!--{{render_field(form.confirm, class_="form-control")}}-->
