from datetime import datetime
from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for, session
from flask_login import current_user, login_required
from database import db, ChatMessage, Repairer, Skill, Ticket, Customer, User
from werkzeug.security import generate_password_hash

customer_r=Blueprint('customer', __name__)



@customer_r.route('/ticket/step1', methods=['GET', "POST"])
@login_required
def ticket_step1():
    if request.method == "POST": 
        session['ticket'] = {'model_series': request.form.get('model_series')}
        return redirect(url_for('customer.ticket_step2'))
    
    skills = Skill.get_modelseries()
    return render_template('ticket_step1_model.html', skills = skills)



@customer_r.route('/ticket/step2', methods=['GET', "POST"])
@login_required
def ticket_step2():
    print("DEBUG: STEP 2 ROUTE HIT")
    print("SESSION VORHER:", session.get('ticket'))

    if 'ticket' not in session:
        flash("Bitte zuerst ein Modell auswählen.")
        return redirect(url_for('customer.ticket_step1'))

    if request.method == 'POST':
        print("DEBUG: POST request erkannt")
        session['ticket']['init_message'] = request.form.get('init_message')
        print("SESSION NACHHER:", session.get('ticket'))
        return redirect(url_for('customer.ticket_step3'))

    return render_template('ticket_step2_init_message.html')



@customer_r.route('/ticket/step3', methods=['GET', 'POST'])
@login_required
def ticket_step3():
    if 'ticket' not in session or 'model_series' not in session['ticket']:
        flash("Bitte wähle zuerst ein Modell.")
        return redirect(url_for('customer.ticket_step1'))

    model = session['ticket']['model_series']

    # Hole alle Reparateur:innen, die das gewählte Modell beherrschen
    repairers = db.session.execute(
        db.select(Repairer)
        .join(Repairer.skills_rl)
        .filter(Skill.model_series == model)
        .join(User)
    ).scalars().all()

    if not repairers:
        flash("Leider wurde kein Reparateur für dieses Modell gefunden.")
        return redirect(url_for('customer.ticket_step1'))

    if request.method == 'POST':
        session['ticket']['repairer_id'] = request.form.get('repairer_id')
        return redirect(url_for('customer.ticket_confirmation'))

    return render_template('ticket_step3_repairer.html', repairers=repairers, model=model)



@customer_r.route('/ticket-bestätigung', methods=['GET','POST'])
@login_required
def ticket_confirmation():
    data = session.get('ticket')
    if not data or not all(k in data for k in ('model_series', 'init_message', 'repairer_id')):
        flash("Ticket-Daten nicht gefunden.")
        return redirect(url_for('customer.ticket_step1'))
    
    # Optional: Reparateur-Namen anzeigen
    repairer = db.session.get(Repairer, int(data['repairer_id']))
    
    if request.method == 'POST':
        ticket = Ticket(
            customer_id = current_user.customer_id,
            model = data['model_series'],
            init_message = data['init_message'],
            repairer_id = data['repairer_id'],
            timestamp = datetime.now() 
        )
        db.session.add(ticket)
        db.session.commit()
        session.pop('ticket', None)  # Clear the session data
        flash("Dein Ticket wurde erfolgreich erstellt.")
        return redirect(url_for('customer.get_tickets'))
    return render_template('ticket_confirmation.html', data=data)



@customer_r.route('/account-information', methods=['GET', 'POST'])
@login_required
def get_account_info():
    if request.method == "POST":
        current_user.first_name = request.form["first_name"]
        current_user.last_name = request.form["last_name"]
        current_user.email = request.form["email"]
        #Quelle für Passwort ändern bei Eingabe,ChatGPT
        new_password = request.form["password"]
        password_confirm =request.form["password_confirm"]
        if new_password.strip():
            if new_password != password_confirm:
                flash("Passwörter stimmen nicht überein", "danger")
                return redirect(url_for("customer.get_account_info"))
            else:
                current_user.password_hash = generate_password_hash(new_password)
        db.session.commit()
        flash("Daten wurden gespeichret")
        return redirect(url_for("customer.get_account_info"))
    return render_template("customer_account.html")


#Nicht Getestet, rendertemplate änder
@customer_r.route('/repairers', methods=['GET'])
@login_required
def get_repairers():
    repaires=db.session.execute(
        db.select(User).
        filter_by(role='repairer').order_by(User.last_name)).scalars()
    
    return render_template('customer_account-html', repaires=repaires)


#Nicht Getestet, rendertemplate änder
@customer_r.route('/filter-by-repairers', methods=['GET'])
@login_required
def filter_by_repairers():
    model_series=request.args.get('skill')
    repaires=db.session.execute(
        db.select(User).
        join(User.repairer).
        join(Repairer.skills_rl).
        where(model_series=model_series)).scalars()
    
    return render_template('customer_account-html', repaires=repaires)


#Nicht Getestet
@customer_r.route('/create-ticket', methods=['POST'])
@login_required
def create_ticket():
    repairer_id=request.args.get('repairer_id')
    model_series=request.args('model_series')
    ticket=Ticket(customer_id=current_user.id, repairer_id=repairer_id, model=model_series)
    db.session.add(ticket)
    db.session.commit()

    return redirect(url_for('customer.filter_by_repaires'))
    


#Nicht Getestet, render template änder
@customer_r.route('/get-tickets', methods=['GET'])
@login_required
def get_tickets():
    tickets=db.session.execute(
        db.select(Ticket).where(customer_id=current_user.id)).scalars()
    
    return render_template('customer_account.html', tickets=tickets)



#Nicht Getestet
@customer_r.route('/delete-ticket/<int:ticket_id>', methods=['POST'])
@login_required
def delete_ticket(ticket_id):
    ticket = db.session.execute(db.select(Ticket).filter_by(ticket_id=ticket_id))
    db.session.delete(ticket)
    db.session.commit()
    
    return redirect (url_for('customer.get_tickets'))
    

#Nicht Getestet, render template ändern
@customer_r.route('/open-chat/<int:ticket_id>', methods=['GET'])
@login_required
def open_chat(ticket_id):
    chat_message=db.session.execute(
        db.select(Ticket).filter_by(ticket_id=ChatMessage.ticket_id)).scalars()
    
    return render_template('chat.html', chat_message)


    



    