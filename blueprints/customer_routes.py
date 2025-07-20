from datetime import datetime
from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for, session
from flask_login import current_user, login_required
from database import db, ChatMessage, Repairer, Skill, Ticket, Customer, User, Rezension
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

#Quelle ChatGPT, hilfe bei der Sessionverwaltung und Ticketerstellung und Debugging
#https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28


@customer_r.route('/ticket/step2', methods=['GET', "POST"])
@login_required
def ticket_step2():

    if 'ticket' not in session:
        flash("Bitte zuerst ein Modell auswählen.")
        return redirect(url_for('customer.ticket_step1'))

    if request.method == 'POST':
        ticket_data = session.get('ticket', {})
        ticket_data['init_message'] = request.form.get('init_message')
        session['ticket'] = ticket_data
        return redirect(url_for('customer.ticket_step3'))

    return render_template('ticket_step2_init_message.html')

#Quelle ChatGPT, hilfe bei der Sessionverwaltung und Ticketerstellung und Debugging
#https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28


@customer_r.route('/ticket/step3', methods=['GET', 'POST'])
@login_required
def ticket_step3():

    if 'ticket' not in session or 'model_series' not in session['ticket']:
        flash("Bitte wähle zuerst ein Modell.")
        return redirect(url_for('customer.ticket_step1'))

    model = session['ticket']['model_series']

    sort = request.args.get('sort')

    # Hole alle Reparateur:innen, die das gewählte Modell beherrschen
    repairers = db.session.execute(
        db.select(Repairer)
        .join(Repairer.skills_rl)
        .filter(Skill.model_series == model)
        .join(User)
    ).scalars().all()

    # Sortiere die Reparateur:innen nach Bewertung
    if sort == 'high':
        repairers.sort(key=lambda r: r.average_rating or 0, reverse=True)
    elif sort == 'low':
        repairers.sort(key=lambda r: r.average_rating or 0)

    # Berechne die durchschnittliche Bewertung für den Reparateur:in mir dem gewählten Modell
    for r in repairers:
        rezensionen = (
            db.session.query(Rezension)
            .join(Ticket)
            .filter(Ticket.repairer_id == r.repairer_id,Ticket.model == model)
            .all()
        )
        if rezensionen:
            r.average_rating = round(sum([rez.stars for rez in rezensionen]) / len(rezensionen), 1)
        else:
            r.average_rating = None

    if not repairers:
        flash("Leider wurde kein Reparateur für dieses Modell gefunden.")
        return redirect(url_for('customer.ticket_step1'))

    if request.method == 'POST':
        ticket_data = session.get('ticket', {})
        ticket_data['repairer_id'] = request.form.get('repairer_id')
        session['ticket'] = ticket_data  
        return redirect(url_for('customer.ticket_confirmation'))

    return render_template('ticket_step3_repairer.html', repairers=repairers, model=model)

#Quelle ChatGPT, hilfe bei der Sessionverwaltung und Ticketerstellung und Debugging
#https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28


@customer_r.route('/ticket-bestätigung', methods=['GET','POST'])
@login_required
def ticket_confirmation():
    data = session.get('ticket')
    if not data or not all(k in data for k in ('model_series', 'init_message', 'repairer_id')):
        flash("Ticket-Daten nicht gefunden.")
        return redirect(url_for('customer.ticket_step1'))
    
    if request.method == 'POST':
        try:
            ticket = Ticket(
                customer_id = current_user.customer.customer_id,
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
        except Exception as e:
            flash("Es gab ein Problem bei der Erstellung deines Tickets. Bitte versuche es erneut.", "danger")
            return redirect(url_for('customer.ticket_step1'))
    
    # Reparateur-Namen anzeigen
    repairer = db.session.get(Repairer, int(data['repairer_id']))
    return render_template('ticket_confirmation.html', data=data, repairer=repairer)

#Quelle ChatGPT, hilfe bei der Sessionverwaltung und Ticketerstellung und Debugging
#https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28


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
        flash("Daten wurden gespeichret", "success")
        return redirect(url_for("customer.get_account_info"))
    return render_template("customer_account.html")



@customer_r.route('/get-tickets', methods=['GET'])
@login_required
def get_tickets():
    status = request.args.get('status')  # open / finished
    query = db.select(Ticket).filter_by(customer_id=current_user.customer.customer_id)

    if status == 'open':
        query = query.filter(Ticket.finished == False)
    elif status == 'finished':
        query = query.filter(Ticket.finished == True)
    elif status == 'declined':
        query = query.filter(Ticket.accepted == False)

    tickets = db.session.execute(query.order_by(Ticket.timestamp.desc())).scalars().all()

    return render_template('get_tickets.html', tickets=tickets, status=status)




    



    