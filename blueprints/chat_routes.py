from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from database import db, ChatMessage, Ticket

chat_r =Blueprint('chat', __name__)

@chat_r.route('/chat/ticket/<int:ticket_id>', methods=['GET'])
@login_required
def open_chat(ticket_id):
    ticket = db.session.execute(
        db.select(Ticket).filter_by(ticket_id=ticket_id)
    ).scalar_one_or_none()

    if not ticket:
      if current_user.repairer:
         return redirect(url_for('repairer.get_tickets'))
      elif current_user.customer:
         return redirect(url_for('customer.get_tickets'))
      else:
         flash("Zugriff verweigert.")
         return redirect(url_for('auth.login'))
  
    chat_messages = db.session.execute(
      db.select(ChatMessage).where(ChatMessage.ticket_id == ticket_id).order_by(ChatMessage.timestamp)
    ).scalars().all()

    return render_template('chat.html', ticket=ticket, chat_messages=chat_messages)