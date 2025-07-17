from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from database import User, db, Customer, Repairer, Rezension, Ticket
from datetime import datetime

review_r= Blueprint('review', __name__)

@review_r.route('/ticket/<int:ticket_id>/submit_review', methods=['GET', 'POST'])
@login_required
def submit_review(ticket_id): 
    ticket = db.session.execute(
        db.select(Ticket).filter_by(ticket_id=ticket_id)
    ).scalar_one_or_none()
    
    #if ticket.customer_id != current_user.user_id:
        #flash("Du kannst nur Rezensionen für deine eigenen Tickets schreiben.")
        #return redirect(url_for('customer.get_account_info'))
    
    if request.method == 'POST':
        stars = request.form.get('stars')
        commentar = request.form.get('commentar')

        new_review = Rezension(
            ticket_id=ticket_id,
            stars=int(stars),
            commentar=commentar,
            timestamp=datetime.utcnow()
        )
        
        #if not stars or not commentar:
            #lash("Bitte fülle alle Felder aus.", "danger")
            #return redirect(url_for('review.submit_review', ticket_id=ticket_id))
        
        db.session.add(new_review)
        db.session.commit()
        
        flash("Deine Rezension wurde erfolgreich eingereicht.", "success")
        return redirect(url_for('customer.get_tickets'))
    
    return render_template('submit_review.html', ticket=ticket)


@review_r.route('/repairer/<int:repairer_id>/reviews')
@login_required
def repairer_reviews(repairer_id):
    repairer = db.session.execute(
        db.select(Repairer).filter_by(repairer_id=repairer_id)
    ).scalar_one_or_none()

    if not repairer:
        flash("Reparateur wurde nicht gefunden.", "danger")
        return redirect(url_for('customer.get_tickets'))

    # Alle Rezensionen für diesen Reparateur über die Tickets
    rezensionen = (
        db.session.query(Rezension)
        .join(Ticket)
        .filter(Ticket.repairer_id == repairer_id)
        .order_by(Rezension.timestamp.desc())
        .all()
    )

    return render_template(
        'repairer_reviews.html',
        repairer=repairer,
        rezensionen=rezensionen
    )


