---
title: Authentifizierungs Routen 
parent: Funktionen und Routen
nav_order: 1
---

# Authentifizierungs Routen

<details open markdown="block">

<summary>Authentifizerungs Routen</summary>

- [Authentifizierungs Routen](#authentifizierungs-routen)
    - [register()](#register)
    - [login()](#login)
    - [logout()](#logout)

</details>

### register()

**Route:** /register

**Methoden:** GET, POST

**Zweck:** Damit kann sich ein neuer User registrieren, um die vollen Funktionen der App nutzen zu können. Dabei ist Wichtig das der User alle Felder ausfüllt, und keine E-Mail benutzt, die bereits vorhanden ist.

**Möglicher Output:**

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

**Zweck:** Der User wird von seiner bestehende Session ausgeloggt, und zurück zur Login Seite weitergeleitet.

**Möglicher output:** 

<img src="../../assets/references_assets/logout.png" width="400">



