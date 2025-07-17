---
title: Design Entscheidungen
nav_order: 3
---


# Design Entscheidungen

<details open markdown="block">

<summary>Unsere Design Decisions</summary>

1. Datenbank: Plain-SQL oder SQLAlchemy?
2. Flask-Login oder manuelles Session-Handling?
3. Flask-Routen auslagern?
4. Bootstrap oder manuelles CSS?

</details>

## 01: Datenbank: Plain-SQL oder SQLAlchemy?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 14-06-2025

### Problem

Sollten wir CRUD Befehle in Plain-SQL oder in Python als ORM (object-relational-mapper) in unserem Projekt benutzen?

Unsere Applikation ist in Python mit Flak geschrieben und mit einer SQLite Datenbank verbunden. Ziel dabei ist es, eine langfristige und wartbare Lösung für den Datebankzugriff zu wählen, ohne dabei unnötige Komplexität einzuführen.


### Unsere Entscheidung

Wir haben uns für SQLAlchemy entschieden. Der ORM Ansatz spricht uns mehr an, als reine Plain-SQL. Zum einem erhöht SQLAlchemy die Wartbarkeit und Lesbarkeit einzelner SQL Statemants im ORM Ansatz, da die Datenbanklogik in strukturierten Python Klassen abgebildet wird. Zum anderen sind wir auch dafür offen, Technologien die wir noch nicht benutzt haben in Projekte zu intrigieren trotz anfänglicher Einstiegshürde. SQLAlchemy bietet damit eine moderen und sauber Möglichkeit, mit relationalen Datenbanken zu arbeiten.

### Mögliche Optionen

Wir hatten für den Bereich Datenbanken zwei Optionen:

+ Plain-SQL
+ SQLAlchemy

| Kriterium | Plain-SQL | SQLAlchemy
| :---: | :---: | :---: |
| **Know-How** | ✔️ Wir kennen Plain-SQL aus dem Modul Datenbanken | ❌ Wir müssen uns zuerst mit dem ORM Ansatz auseindersetzen 
| **Lesbarkeit** | ❌ Bei komplexen Anfragen schnell unübersichtlich | ✔️ Auch bei Komplexen Anfragen leserlich
| **Wartung** | ❌ Änderungen an der Datenbankstruktur müssen manuell an jeder Stelle angepasst werden | ✔️ Durch den ORM Ansatz werden Änderung an der Datenbankstruktur vereinfacht 
| **Fehleranfälligkeit** | ❌ Höhere Fehleranfälligkeit durch manuelle SQL Statemants | ✔️ IDE-Unterstützung reduziert typische Tippfehler im Code 
| **Redundanzen** | ❌ Häufig sich wiederholender Code | ✔️ Weniger Redundanzen durch abstrakte CRUD Operationen

## 02: Flask-Login oder manuelles Session-Handling?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 24-06-2025

### Problem

Unser Projekt hat eine Login Funktion intrigiert, um sicherzustellen dass bestimmte Rolen nur auf bestimmte Routen zugreiffen sollen. Ziel dabei soll es sein möglichst einfach eine hohe Sicherheit, sowie hohe Wartbarkeit gewährleisten zu können. 


### Unsere Entscheidung

Wir haben uns für Flask-Login entschieden, statt den Login manuell zu handhaben. Manuelles Session-Handling ist einfach viel zu Fehleranfällig und hat viele Redundanzen im Code. Flask-Login hingegen bietet eine sehr gute alternative zum einfachen Login und Session-Handling. 

### Mögliche Optionen

Wir hatten für den Bereich Login und Session-Handling zwei Optionen:

+ Manuelles Session-Handling
+ Flask-Login

| Kriterium | Manuelles Session-Handling | Flask-Login
| :---: | :---: | :---: |
| **Know-How** | ❌ Kaum vorhanden, Umsetzung muss selbst recherchiert werden | ✔️Kaum vorhanden, aber gut dokumentiert
|**Komplexität**| ❌ Hoch, Session-Handling muss selbst gebaut werden | ✔️ Niedrig mit wenigen Zeilen Code
|**Fehleranfälligkeit**| ❌ Durch redundanten Code hoch | ✔️ Sehr gering durch Funktionen die Flask-Login bereitstellt 
|**Routenschutz**| ❌ Checks in den Routen nötig | ✔️ Bequem durch @login_required


## 03: Flask-Routen auslagern?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 21-06-2025

### Problem

In einem Projekt was wächst führt das definieren der Routen in einer einzigen File schnell zu Problemen hinsichtlich der Übersichlickeit, Skalierbarkeit und Wartbarkeit. Bei zunehmender Komplexität des Projektes und das hinzufügen weitere Features wie zum Beispiel Rezensionen oder Chats, wird der Code der Routen in einer einzige File schwer lesbar und man kann nicht schnell genug zu bestimmten Routen navigiern wenn die Routen zum Beispiel einen Umfang von 1500 Zeilen Code haben.


### Unsere Entscheidung

Wir haben zuerst überlegt ob wir die Routen in einer einzigen File auslagern, statt sie in der Main zu definieren. Doch uns wurde schnell klar, dass auch diese Lösung nicht zum gewünschten Ergebniss führt. Daher haben wir uns dazu entschieden, die Routen nach Use-Case und User-Gruppe auszulagern. Die führt zu einer viel bessern Wartung des Codes. 

### Mögliche Optionen

Wir hatten für den Bereich Routen Auslagern drei Optionen:

+ Alle Routen in der Main
+ Alle Routen in einer einzigen File
+ Routen nach Use-Case und User-Gruppe auslagern

| Kriterium | Alle Routen in der Main | Alle Routen in einer einzigen File | Routen nach Use-Case und User-Gruppe auslagern
| :---: | :---: | :---: | :---: |
| **Lesbarkeit**| ❌ Routen gehen unter anderem Code unter | ❌ Besser, aber bei viele Routen immer noch unübersichtlich | ✔️ Sehr gut, Routen werden sauber strukturiert
| **Warbarkeit**| ❌ Änderungen erforden lange Suche Code | ❌ Änderung erfordern lange Suche bei viel Code | ✔️ Änderungen sind lokal in der Datei mit wenig Code 
|**Erweiterbarkeit** | ❌ Alles muss zentral ergänzt werden | ❌ Bei viel Code immer noch schwer Erweiterbar | ✔️ Neue Use-Case/Funktionen lassen sich leicht lokal intrigieren

## 04: Bootstrap oder manuelles CSS?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 21-06-2025



## 04: Bootstrap oder manuelles CSS?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 22.06.2025

### Problem 

In unserem Projekt wollen wir ein benutzerfreundliches Design gewährleisten. Die Frage hierbei ist, ob wir dies manuelle und aufwendig gestalten, oder auf ein bestehendes Framework wie Bootstrap zurückgreifen. Ziel dabei ist es, die UI effizient und wartbar zu gestalten.


### Unsere Entscheidung

Wir haben uns für Bootstrap entschieden, da es einen sehr schnellen Start für solide Designs und UI Komponeten ermöglicht. Das manuelle schreiben von CSS wäre hier aufwendiger und mehr fehleranfällig.

### Mögliche Entscheidungen

Wir hatten für den Bereich Styling und CSS hatten wir zwei Optionen:

+ Manuelles CSS
+ Bootstrap Framework

| Kriterium | Manuelles CSS | Bootstrap Framework
| :---: | :---: | :---: |
| **Know-How** | ❌ Teilweise vorhanden, aber hoher Aufwand für komplexe UI's| ✔️Sehr gute Dokumentation
|**Komplexität**| ❌ Hoch, bei komplexem Design und Komponenten | ✔️ Gering durch vorgefertigte Komponenten
|**Entwicklunggeschwindikeit**| ❌ Langsam durch's selbst schreiben | ✔️ Schnell durch vorgefertigte Komponenten
|**Design-Konsistenz**| ❌ Muss immer sichergestellt sein | ✔️ Durch Framework automatisch gegeben





<!---
Quelle von: https://github.com/hwrberlin/fswd-app/blob/main/docs/design-decisions.md letzter Zugriff am: 12.06.2025
-->