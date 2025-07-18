from flask import Flask, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from database import db, ChatMessage, Ticket
from datetime import datetime

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

@chat_r.route('/chat/send', methods=['POST'])
@login_required
def send_message():
  ticket_id = request.form.get('ticket_id')
  content = request.form.get('content')

  if not ticket_id or not content:
    flash("Nachricht konnte nicht gesendet werden")
    return redirect(url_for('chat.open_chat', ticket_id=ticket_id))
   
  ticket = db.session.execute(
    db.select(Ticket).filter_by(ticket_id=ticket_id)
  ).scalar_one_or_none()

  if not ticket:
    flash("Ticket nicht gefunden.")
    return redirect(url_for('chat.open_chat', ticket_id=ticket_id))
   
  if current_user.repairer:
    sender_role = "repairer"
  elif current_user.customer:
     sender_role = "customer"
  else:
     flash("Unbekannte Benutzerrolle.")
     return redirect(url_for('auth.login'))
  
  message = ChatMessage(
     ticket_id = ticket_id,
     message = content,
     timestamp = datetime.now(),
     sender_role = sender_role
  )
  db.session.add(message)
  db.session.commit()

  return redirect(url_for('chat.open_chat', ticket_id=ticket_id))
