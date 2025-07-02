from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from database import ChatMessage, db, Repairer, Skill, Ticket, User
from werkzeug.security import generate_password_hash


repairer_r=Blueprint('repairer', __name__)



@repairer_r.route('/accountinformation', methods=['GET', 'POST'])
@login_required
def get_account_info():
    if request.method == "POST":
        current_user.first_name = request.form["first_name"]
        current_user.last_name = request.form["last_name"]
        current_user.email = request.form["email"]
        #Quelle für Passwort ändern bei Eingabe,ChatGPT
        new_password = request.form["password"]
        password_confirm = request.form["password_confirm"]
        if new_password.strip():
            if new_password != password_confirm:
                flash("Passwörter stimmen nicht überein", "danger")
                return redirect(url_for("repairer.get_account_info"))
            else:
                current_user.password_hash = generate_password_hash(new_password)
        db.session.commit()
        flash("Daten wurden gespeichert", "success")
        return redirect(url_for("repairer.get_account_info"))
    return render_template("repairer_account.html")

#Nicht getestet
@repairer_r.route('/meine-skills', methods=['GET'])
@login_required
def show_skills():
    repairer=db.session.execute(
        db.select(Repairer).filter_by(user_id=current_user.user_id)).scalar_one()
    skills=repairer.skills_rl
    all_skills=db.session.execute(db.select(Skill)).scalars().all()

    return render_template('repairer_skills.html', skills=skills, all_skills=all_skills)


@repairer_r.route('/skills-hinzufügen', methods=['POST'])
@login_required
def add_skills():
   skill_id = request.form['skill_id']
   skill = db.session.execute(
       db.select(Skill).filter_by(skill_id=skill_id)).scalar_one()
   repairer=db.session.execute(
       db.select(Repairer).filter_by(user_id=current_user.user_id)).scalar_one()
   
   if skill not in repairer.skills_rl:
        repairer.skills_rl.append(skill)
        db.session.commit()

   return redirect(url_for('repairer.show_skills'))


@repairer_r.route('/skills-löschen', methods=['POST'])
@login_required
def delete_skills():
    skill_id = request.form['skill_id']
    skill = db.session.execute(
        db.select(Skill).filter_by(skill_id=skill_id)).scalar_one()
    repairer=db.session.execute(
        db.select(Repairer).filter_by(user_id=current_user.user_id)).scalar_one()
    
    if skill in repairer.skills_rl:
        repairer.skills_rl.remove(skill)
        db.session.commit()
    
    return redirect(url_for('repairer.show_skills'))
        
@repairer_r.route('/meine-anfragen', methods=['GET'])
@login_required
def get_tickets():
    tickets=db.session.execute(db.select(Ticket).where(Ticket.repairer_id==current_user.user_id)).scalars().all()

    return render_template('repairer_requests.html', tickets=tickets)


@repairer_r.route('/ticket-annehmen',methods=['POST'])
@login_required
def accept_ticket(ticket_id):
    ticket=db.session.execute(db.select(Ticket).filter_by(ticket_id=ticket_id)).scalar_one()
    ticket.accepted=True
    db.session.commit()
    return redirect(url_for(''))

@repairer_r.route('/ticket-ablehen', methods=['POST'])
@login_required
def decline_ticket(ticket_id):
    ticket=db.session.execute(db.select(Ticket).filter_by(ticket_id=ticket_id))
    ticket.accpted=False
    db.session.commit()
    return redirect(url_for(''))

@repairer_r.route('/chat-öffnen', methods=['POST'])
@login_required
def open_chat(ticket_id):
    chat_message=db.session.execute(
        db.select(Ticket).filter_by(ticket_id=ChatMessage.ticket_id)).scalars().all()
    
    return render_template('chat.html', chat_message)
    

    













