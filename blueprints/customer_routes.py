from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from database import db, ChatMessage, Repairer, Skill, Ticket, Customer, User

customer_r=Blueprint('customer', __name__)


#Nicht getestet, template ändern
@customer_r.route('/account-information/<int:user_id>', methods=['GET'])
@login_required
def get_account_information(user_id):
    cur_user=db.session.execute(
        db.select(User).
        filter_by(user_id=current_user.user_id)).scalar()
    
    return render_template('customer_account.html', cur_user=cur_user)


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


    



    