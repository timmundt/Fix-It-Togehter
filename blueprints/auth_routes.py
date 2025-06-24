from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import User, db, Customer, Repairer

auth_r= Blueprint('auth', __name__)

#Nicht fertig
@auth_r.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        
        if not user:
            flash('Ungültige Email Adresse!')
            return redirect(url_for('auth_r.login'))
        
        if not check_password_hash(user.password_hash, password):
            flash('Ungültiges Passwort!')
            return redirect(url_for('auth_r.login'))
        
        customer=Customer.query.filter_by(customer_id=user.user_id).first()
        repairer=Repairer.query.filter_by(customer_id=user.user_id).first()
        login(user)

        if customer:
            return render_template('customer_account.html')
        
        if repairer:
            return render_template('repairer_account.html')
    
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
        
        if User.query.filter_by(email=email).first():
            flash('Email bereits vorhanden!')
            return redirect(url_for('auth_r.register'))
        
        user=User(last_name=last_name,first_name=first_name,email=email, password_hash=password_hash, role=role)
        db.session.add(user)
        db.session.commit()
        
        if role == 'customer':
            customer=Customer(customer_id=user.user_id)
            db.session.add(customer)
            db.session.commit()
            return redirect(url_for('auth_r.login'))
        
        if role == 'repairer':
            repairer=Repairer(repairer_id=user.user_id)
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
    