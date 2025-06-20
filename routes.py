from flask import Flask, Blueprint, flash, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, Customer, Repairer

main=Blueprint('main',__name__)

@main.route('/')
def home():
    return render_template('index.html')


@main.route('/startseite')
def return_home():
    return render_template('index.html')

#Nicht fertig
@main.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
    
    else:
        return render_template('login.html')


#Nicht fertig 
@main.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        last_name=request.form.get('last_name')
        first_name=request.form.get('first_name')
        email=request.form.get('email')
        password=request.form.get('password')
        role=request.form.get('role')
        password_hash=generate_password_hash(password)
        
        if Customer.query.filter_by(email=email).first() or Repairer.query.filter_by(email=email).first():
            return ""
        
        if role == 'customer':
            customer=Customer(last_name=last_name,first_name=first_name,email=email, password_hash=password_hash)
            db.session.add(customer)
            db.session.commit()
            return redirect
        
        if role == 'repairer':
            repairer=Repairer(last_name=last_name, first_name=first_name,email=email,password_hash=password_hash)
            db.session.add(repairer)
            db.session.commit()
            return redirect
    
    return render_template('register.html')
        







