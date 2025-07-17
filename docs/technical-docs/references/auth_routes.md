---
title: Authenticate Routes
parent: References
nav_order: 1
---

### register()

**Route:** /register

**Methods:** GET, POST

**Purpose:** Damit kann sich ein neuer User registriren, um die vollen Funktionen der App nutzen zu können. Dabei ist Wichtig das der User alle Felder ausfüllt, und keine E-Mail benutzt, die bereits vorhanden ist.

**Sample output:**

**Sucess:** 

**Error:**

<img src="../../assets/references_assets/error_register.png " width="400"/>

### login()

**Route:** /login

**Methods:** GET, POST

**Purpose:** Mit dieser Route kann sich der Nutzer einloggen, wenn er bereits ein Bestehenden Account hat. Wenn er sich erfolgreich eingeloggt hat, wird er auf seine Account-Informationsseite weitergeleitet. Gibt er die E-Mail oder das Passwort falsch ein, erscheint eine Fehlermeldung.

**Sample output:** 

**Sucess**

<img src="../../assets/references_assets/sucess_login.png" width="600"/>

**Error:**

<img src="../../assets/references_assets/error_login.png" width="400">

### logout()

**Route:** /logout

**Methods:** GET, POST

**Purpose:** Der User wird von seiner bestehende Session ausgeloggt, und zurück zur Login Seite weitergeleitet.

**Sample output:** 

<img src="../../assets/references_assets/logout.png" width="400">



