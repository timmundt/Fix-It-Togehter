from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Date, DateTime, ForeignKey, LargeBinary, Null, orm, Column, Integer, String
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    user_id=Column(Integer,primary_key=True,index=True)
    last_name=Column(String,nullable=False)
    first_name=Column(String, nullable=False)
    email=Column(String,nullable=False, unique=True,index=True)
    password_hash=Column(String,nullable=False)
    role=Column(String, nullable=False)

    customer=db.relationship('Customer', backref='user', uselist=False)
    repairer=db.relationship('Repairer', backref='user', uselist=False)

    def get_id(self):
        return str(self.user_id)


class Customer(db.Model): 
    customer_id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey('user.user_id'), nullable=False)
    
    ticket_rl=db.relationship('Ticket', backref='customer')


class Repairer(db.Model):
    repairer_id=Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey('user.user_id'), nullable=False)

    ticket_rl=db.relationship('Ticket',backref='repairer')
    skills_rl=db.relationship('Skill', secondary='repairer_skill', backref='repairer')


class Rezension(db.Model):
    rezension_id=Column(Integer, primary_key=True, index=True)
    ticket_id=Column(Integer,ForeignKey('ticket.ticket_id'), nullable=False)
    stars=Column(Integer, nullable=False)
    commentar=Column(String)
    timestamp=Column(DateTime, nullable=False)

    ticket_rl=db.relationship('Ticket', backref=db.backref('rezension', uselist=False))


class Skill(db.Model):
    skill_id=Column(Integer, primary_key=True, index=True)
    model_series=Column(String, nullable=False)

    @classmethod
    def get_modelseries(cls):
        all_skills=db.session.execute(
            db.select(cls.model_series)).scalars().all()
        return all_skills
    
    


class Ticket(db.Model):
    ticket_id=Column(Integer, primary_key=True, index=True)
    customer_id=Column(Integer, ForeignKey('customer.customer_id'),nullable=False)
    repairer_id=Column(Integer, ForeignKey('repairer.repairer_id'),nullable=False)
    model=Column(String, nullable=False)
    init_message=Column(String, nullable=False)
    timestamp=Column(Date, nullable=False)
    accepted=Column(Boolean, nullable=True, default=None)
    finished=Column(Boolean, default=False)



class ChatMessage(db.Model):
    chat_id=Column(Integer, primary_key=True)
    ticket_id=Column(Integer, ForeignKey('ticket.ticket_id'),nullable=False)
    message=Column(String, nullable=False)
    timestamp=Column(DateTime, nullable=False)
    picture=Column(LargeBinary)
    sender_role=Column(String, nullable=False)

    ticket_rl=db.relationship('Ticket', backref='chatmessage')



repairer_skill =db.Table(
   'repairer_skill',
   db.Column('repairer_id',Integer, ForeignKey('repairer.repairer_id'), nullable=False,primary_key=True),
   db.Column('skill_id',Integer,ForeignKey('skill.skill_id'), nullable=False,primary_key=True)
   
    )


def insert_skills():
    if not db.session.execute(db.select(Skill)).first():
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

def insert_dummy_data(): 

    if not db.session.execute(db.select(User)).first():
    
        user1=User(last_name='Müller', first_name='Max', email='repairer1@test.com', password_hash=generate_password_hash('0000'),role='repairer')
        user2=User(last_name='Mustermann', first_name='Max', email='repairer2@test.com', password_hash=generate_password_hash('0000'),role='repairer')
        user3=User(last_name='Celik', first_name='Baran', email='customer1@test.com', password_hash=generate_password_hash('0000'),role='customer')
        user4=User(last_name='Güney', first_name='Denizcan',email='customer2@test.com',password_hash=generate_password_hash('0000'),role='customer')
        repairer1=Repairer(user=user1)
        repairer2=Repairer(user=user2)
        customer1=Customer(user=user3)
        customer2=Customer(user=user4)

        skills=db.session.execute(db.select(Skill)).scalars().all()

        repairer1.skills_rl.extend([skills[0],skills[1], skills[2]])
        repairer2.skills_rl.extend([skills[3],skills[4],skills[5]])

        db.session.add_all([user1,user2,user3,user4,repairer1,repairer2,customer1,customer2])
        db.session.commit()

        ticket1=Ticket(customer_id=customer1.customer_id, repairer_id=repairer1.repairer_id, model=skills[0].model_series, 
                       init_message="Nur wasser kommt raus",timestamp=datetime.now())
        ticket2=Ticket(customer_id=customer2.customer_id, repairer_id=repairer1.repairer_id, model=skills[1].model_series,
                       init_message="Wenig Wasser kommt raus",timestamp=datetime.now())
        ticket3=Ticket(customer_id=customer1.customer_id, repairer_id=repairer1.repairer_id, model=skills[1].model_series,
                       init_message="Kaffeemaschine geht nichtan", timestamp=datetime.now())
        
        db.session.add_all([ticket1,ticket2,ticket3])
        db.session.commit()


                






