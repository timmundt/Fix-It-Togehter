from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, Customer, Repairer

auth_r= Blueprint('auth', __name__)

#Nicht fertig
@auth_r.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        customer=Customer.getbyemail(email)
        repairer=Repairer.getbyemail(email)

        if not repairer and not customer:
            flash('Ungültige Email Adresse!')
        
        if customer and check_password_hash(customer.password_hash, password):
            login_user(customer)
            return render_template('customer_account.html')
        
        if repairer and check_password_hash(repairer.password_hash, password):
            login_user(repairer)
            return redirect('repairer_account.html')
        
        flash('Ungültiges Passwort!')
        return redirect()
    
    else:
        return render_template('login.html')


#Nicht fertig 
@auth_r.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        last_name=request.form.get('last_name')
        first_name=request.form.get('first_name')
        email=request.form.get('email')
        password=request.form.get('password')
        role=request.form.get('role')
        password_hash=generate_password_hash(password)
        
        if Customer.getbyemail(email) or Repairer.getbyemail(email):
            return flash("Email bereits vorhanden")
        
        if role == 'customer':
            customer=Customer(last_name=last_name,first_name=first_name,email=email, password_hash=password_hash)
            db.session.add(customer)
            db.session.commit()
            return redirect(url_for('auth_r.login'))
        
        if role == 'repairer':
            repairer=Repairer(last_name=last_name, first_name=first_name,email=email,password_hash=password_hash)
            db.session.add(repairer)
            db.session.commit()
            return redirect(url_for('auth_r.login'))
    
    return render_template('register.html')


@auth_r.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Du wurdest erfolgreich ausgeloggt!')
    return redirect(url_for('staticpages.home'))
    