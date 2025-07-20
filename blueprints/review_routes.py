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
    
    
    if request.method == 'POST':
        stars = request.form.get('stars')
        commentar = request.form.get('commentar')

        new_review = Rezension(
            ticket_id=ticket_id,
            stars=int(stars),
            commentar=commentar,
            timestamp=datetime.utcnow()
        )
        

        
        db.session.add(new_review)
        db.session.commit()
        
        flash("Deine Rezension wurde erfolgreich eingereicht.", "success")
        return redirect(url_for('customer.get_tickets'))
    
    return render_template('submit_review.html', ticket=ticket)

#Quelle für die Reviewerstellung-Route: https://chatgpt.com/share/687be667-3568-8005-9ebd-c42d425b8360

@review_r.route('/repairer/<int:repairer_id>/reviews')
@login_required
def repairer_reviews(repairer_id):
    model = request.args.get("model")

    repairer = db.session.execute(
        db.select(Repairer).filter_by(repairer_id=repairer_id)
    ).scalar_one_or_none()

    if not repairer:
        flash("Reparateur wurde nicht gefunden.", "danger")
        return redirect(url_for('customer.get_tickets'))

    #Alle Rezensionen für den Reparateur und das Modell abrufen
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
        rezensionen=rezensionen,
        model=model
    )

#Quelle für die Anzeigefunktion aller Rezension für den Reparateur mit dem Modell: https://chatgpt.com/share/687cc85e-8760-8005-a71a-6fdb9f03e4e6
