from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Date, DateTime, ForeignKey, LargeBinary, Null, orm, Column, Integer, String

db = SQLAlchemy()


class Customer(db.Model, UserMixin): 
    __tablename__ = 'customer'
    customer_id=Column(Integer, primary_key=True, index=True)
    last_name=Column(String, nullable=False)
    first_name=Column(String,nullable=False)
    email=Column(String, nullable=False, unique=True, index=True)
    password_hash=Column(String, nullable=False)

    ticket_rl=db.relationship('Ticket', backref='customer')

    def getbyemail(cls, email):
        return cls.query.filter_by(email=email).first()


class Repairer(db.Model, UserMixin):
    __tablename__ = 'repairer'
    repairer_id=Column(Integer, primary_key=True)
    last_Name=Column(String, nullable=False)
    first_name=Column(String, nullable=False)
    email=Column(String, nullable=False, unique=True, index=True)
    password_hash=Column(String, nullable=False)

    ticket_rl=db.relationship('Ticket',backref='repairer')
    skills_rl=db.relationship('Skill', secondary='repairer_skill', backref='repairer')

    @classmethod
    def getbyemail(cls, email):
        return cls.query.filter_by(email=email).first()
    
    


class Rezension(db.Model):
    __tablename__='rezension'
    rezension_id=Column(Integer, primary_key=True)
    ticket_id=Column(Integer,ForeignKey('ticket.ticket_id'), nullable=False)
    stars=Column(Integer, nullable=False)
    commentar=Column(String)
    timestamp=Column(DateTime, nullable=False)

    skills_rl=db.relationship('Ticket', backref=db.backref('rezension', uselist=False))


class Skill(db.Model):
    __tablename__ = 'skill'
    skill_id=Column(Integer, primary_key=True)
    model_series=Column(String, nullable=False)


class Ticket(db.Model):
    __tablename__ = 'ticket'
    ticket_id=Column(Integer, primary_key=True)
    customer_id=Column(Integer, ForeignKey('customer.customer_id'),nullable=False)
    repairer_id=Column(Integer, ForeignKey('repairer.repairer_id'),nullable=False)
    modell=Column(String, nullable=False)
    accepted=Column(Boolean, nullable=True, default=None)
    finished=Column(Boolean, default=False)


class ChatMessage(db.Model):
    __tablename__='chatmessage'
    chat_id=Column(Integer, primary_key=True)
    ticket_id=Column(Integer, ForeignKey('ticket.ticket_id'),nullable=False)
    message=Column(String, nullable=False)
    timestamp=Column(DateTime, nullable=False)
    picture=Column(LargeBinary)

    ticket_rl=db.relationship('Ticket', backref='chatmessage')



repairer_skill =db.Table(
   'repairer_skill',
   db.Column('repairer_id',Integer, ForeignKey('repairer.repairer_id'), nullable=False,primary_key=True),
   db.Column('skill_id',Integer,ForeignKey('skill.skill_id'), nullable=False,primary_key=True)
   
    )


def insert_skills():
    if not Skill.query.first():
        skills = [
            Skill(model_series='Magnifica S'),
            Skill(model_series='Magnifica Start'),
            Skill(model_series='Magnifica Evo'),
            Skill(model_series='Magnifica Plus'),
            Skill(model_series='Dinamica'),
            Skill(model_series='Dinamica Plus'),
            Skill(model_series='Eletta Cappucino'),
            Skill(model_series='Eletta Explore'),
            Skill(model_series='Rivelia'),
            Skill(model_series='PrimaDonna Class'),
            Skill(model_series='PrimaDonna Elite '),
            Skill(model_series='PrimaDonna Soul'),
            Skill(model_series='PrimaDonna Aromatic'),
            Skill(model_series='Maestosa'),
            Skill(model_series='Dedica'),
            Skill(model_series='Dedica Plus'),
            Skill(model_series='La Specialista Arte Evo'),
            Skill(model_series='La Specialista Maestro'),
            Skill(model_series='La Specialista Arte Opera'),
            Skill(model_series='ECP'),
            Skill(model_series='COM'),
            Skill(model_series='Clessidra'),
            Skill(model_series='Nespresso'),
            Skill(model_series='Dolce Gusto')
        ]
        db.session.add_all(skills)
        db.session.commit()





