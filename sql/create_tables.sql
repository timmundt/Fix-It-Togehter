CREATE TABLE customer(
customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
last_name TEXT NOT NULL,
first_name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE, 
password_hash TEXT NOT NULL,
);

CREATE TABLE repairer(
repairer_id INTEGER PRIMARY KEY AUTOINCREMENT,
last_name TEXT NOT NULL,
first_name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
password_hash TEXT NOT NULL 
);

CREATE TABLE skills(
skills_id INTEGER PRIMARY KEY AUTOINCREMENT,
repairer_id INTEGER NOT NULL 
brand TEXT NOT NULL, 
machine_type TEXT NOT NULL,
UNIQUE (repairer_id, brand, machine_type),
FOREIGN KEY (repairer_id) REFERENCES repairer (repairer_id)
);

CREATE TABLE ticket (
ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_id INTEGER,
repairer_id INTEGER,
modell TEXT NOT NULL,
text_message TEXT NOT NULL,
FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
FOREIGN KEY (repairer_id) REFERENCES repairer (repairer_id)
);