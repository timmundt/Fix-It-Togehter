from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from database import Repairer, Skill, Ticket, User


repairer_r=Blueprint('repairer', __name__)

db=SQLAlchemy()


#Nicht getestet
@repairer_r.route('/accountinformation', methods=['GET'])
@login_required
def get_account_information():
    repiarer=db.session.execute(db.select(User).filter_by(user_id=current_user.user_id)).one()
    return render_template('repairer_account.html', repairer=repiarer)

#Nicht getestet
@repairer_r.route('/meine-anfragen', methods=['GET'])
@login_required
def get_repairer_tickets():
    repairer=db.session.execute(db.select(Repairer).filter_by(user_id=current_user.user_id)).one()
    tickets=repairer.ticket_rl

    return render_template('repairer_account.html', tickets=tickets)

#Nicht getestet
@repairer_r.route('/meine-skills', methods=['GET'])
@login_required
def show_skills():
    repairer=db.session.execute(db.select(Repairer).filter_by(user_id=current_user.user_id)).one()
    skills=repairer.skills_rl
    all_skills=db.session.execute(db.select(Skill)).scalars()

    return render_template('repairer_account.htmnl', skills=skills, all_skills=all_skills)


@repairer_r.route('skills-hinzufügen', methods=['POST'])
@login_required
def add_skills(skill_id):
   repairer=db.session.execute(db.select(Repairer).filter_by(user_id=current_user.user_id)).one()
   repairer_skill= repairer_skill()


@repairer_r.route('skill-löschen', methods=['POST'])
@login_required
def delete_skill(skill_id):
    repairer=db.session.execute(db.select(Repairer).filter_by(user_id=current_user.user_id)).one()














