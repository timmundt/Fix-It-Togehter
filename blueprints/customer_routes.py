from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from database import Repairer, Skill, Ticket, Customer

customer_r=Blueprint('customer_r', __name__)

db =SQLAlchemy()



@customer_r.route('/filter-by-repairers', methods=['GET'])
@login_required
def filter_by_repairers():
    model_series=request.args.get('skill')
    query=Repairer.query.join(Repairer.skills_rl).filter(Skill.model_series==model_series)
    repaires= query.all()
    return render_template('customer_account-html', repaires=repaires)


#Nicht Fertig
@customer_r.route('/create-ticket', methods=['POST'])
@login_required
def createticket():
    repairer_id=request.args.get('repairer_id')
    model_series=request.args('model_series')
    ticket=Ticket(customer_id=current_user.customer_id, repairer_id=repairer_id, model=model_series)
    db.session.add(ticket)
    db.session.commit()

    return redirect(url_for('customer_r.filter_by_repaires'))
    



#Nicht Fertig
##@customer_r.route('/get-tickets', methods=['GET'])
##def gettickets():
    


#Nicht Fertig
#@customer_r.route('/delete-ticket/<id>', methdos=['POST'])
#def deleteticket():
    

#@customer_r.route('/open-chat/<id>', methods=['GET'])
#def openchat():
    