from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from database import User, db, Customer, Repairer

auth_r= Blueprint('auth', __name__)



@auth_r.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()
        
        if not user:
            flash('Ungültige Email Adresse!')
            return redirect(url_for('auth.login'))
        
        if not check_password_hash(user.password_hash, password):
            flash('Ungültiges Passwort!')
            return redirect(url_for('auth.login'))
        
        customer=db.session.execute(db.select(Customer).filter_by(user_id=user.user_id)).scalar_one_or_none()
        repairer=db.session.execute(db.select(Repairer).filter_by(user_id=user.user_id)).scalar_one_or_none()
        login_user(user)

        if customer:
            return redirect(url_for("customer.get_account_info"))
        
        if repairer:
            return redirect(url_for("repairer.get_account_info"))
    
    else:
        return render_template('login.html')



@auth_r.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        last_name=request.form.get('last_name')
        first_name=request.form.get('first_name')
        email=request.form.get('email')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm_password')
        role=request.form.get('role')
        password_hash=generate_password_hash(password)
        
        if db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none():
            flash('Email bereits vorhanden!')
            return redirect(url_for('auth.register'))
        
        if password != confirm_password:
            flash('Passwörter stimmen nicht überein!')
            return redirect(url_for('auth.register'))
        
        user=User(last_name=last_name,first_name=first_name,email=email, password_hash=password_hash, role=role)
        db.session.add(user)
        db.session.commit()
        
        if role == 'customer':
            customer=Customer(user=user)
            db.session.add(customer)
            db.session.commit()
            return redirect(url_for('auth.login'))
        
        if role == 'repairer':
            repairer=Repairer(user=user)
            db.session.add(repairer)
            db.session.commit()
            return redirect(url_for('auth.login'))
    
    return render_template('register.html')



@auth_r.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Du wurdest erfolgreich ausgeloggt!')
    return redirect(url_for('auth.login'))
    