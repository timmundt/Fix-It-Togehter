from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from database import db, Repairer, Skill, Ticket, User
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
        if new_password.strip():
            current_user.password_hash = generate_password_hash(new_password)
        db.session.commit()
        flash("Daten wurden gespeichert")
        return redirect(url_for("repairer.get_account_info"))
    return render_template("repairer_account.html")

#Nicht getestet
@repairer_r.route('/meine-anfragen', methods=['GET'])
@login_required
def get_repairer_tickets():
    repairer=db.session.execute(
        db.select(Repairer).filter_by(user_id=current_user.user_id)).scalar()
    tickets=repairer.ticket_rl

    return render_template('repairer_account.html', tickets=tickets)

#Nicht getestet
@repairer_r.route('/meine-skills', methods=['GET'])
@login_required
def show_skills():
    repairer=db.session.execute(
        db.select(Repairer).filter_by(user_id=current_user.user_id)).one()
    skills=repairer.skills_rl
    all_skills=db.session.execute(db.select(Skill)).scalars().all()

    return render_template('repairer_account.html', skills=skills, all_skills=all_skills)


@repairer_r.route('/skills-hinzufügen', methods=['POST'])
@login_required
def add_skills(skill_id):
   skill_id = request.form['skill_id']
   skill = db.session.execute(
       db.select(Skill).filter_by(skill_id=skill_id)).scalar_one()
   repairer=db.session.execute(
       db.select(Repairer).filter_by(user_id=current_user.user_id)).scalar_one()
   
   if skill not in repairer.skills_rl:
        repairer.skills_rl.append(skill)
        db.session.commit()

   return redirect(url_for('repairer.show_skills'))


@repairer_r.route('/skill-löschen', methods=['POST'])
@login_required
def delete_skill(skill_id):
    skill_id = request.form['skill_id']
    skill = db.session.execute(
        db.select(Skill).filter_by(skill_id=skill_id)).scalar_one()
    repairer=db.session.execute(
        db.select(Repairer).filter_by(user_id=current_user.user_id)).scalar_one()
    
    if skill in repairer.skills_rl:
        repairer.skills_rl.remove(skill)
        db.session.commit()
    
    return redirect(url_for('repairer.show_skills'))
        














