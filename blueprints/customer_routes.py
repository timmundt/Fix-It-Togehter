from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from database import Repairer, Skill, Ticket, Customer

customer_r=Blueprint('customer_r', __name__)

db =SQLAlchemy()


#Nicht Getestet
@customer_r.route('/filter-by-repairers', methods=['GET'])
@login_required
def filter_by_repairers():
    model_series=request.args.get('skill')
    repaires=Repairer.query.join(Repairer.skills_rl).filter(Skill.model_series==model_series).all()
    return render_template('customer_account-html', repaires=repaires)


#Nicht Getestet
@customer_r.route('/create-ticket', methods=['POST'])
@login_required
def create_ticket():
    repairer_id=request.args.get('repairer_id')
    model_series=request.args('model_series')
    ticket=Ticket(customer_id=current_user.customer_id, repairer_id=repairer_id, model=model_series)
    db.session.add(ticket)
    db.session.commit()

    return redirect(url_for('customer_r.filter_by_repaires'))
    


#Nicht Getestet
@customer_r.route('/get-tickets', methods=['GET'])
@login_required
def get_tickets():
    tickets=Ticket.query.filter_by(customer_id=current_user.customer_id).all()
    return render_template('customer_account.html', tickets=tickets)



#Nicht Getestet
@customer_r.route('/delete-ticket/<int:ticket_id>', methods=['POST'])
@login_required
def deleteticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    return redirect (url_for('customer_r.get_tickets'))
    


#@customer_r.route('/open-chat/<int:chat_id>', methods=['GET'])
#@login_required
#def openchat():

    