from flask import render_template,request,redirect,url_for
from northwind import application


@application.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html')