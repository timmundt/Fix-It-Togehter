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
5. Wie soll die Templatestruktur aussehen?
6. Gemeinsames User-Modell oder getrennte Rollen in der Datenbank?
7. Braucht man ein Login, um den vollen Funktionsumfang der Website benutzen zu können?
8. Wer soll das Ticket als beendet markieren?

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

## 05: Wie soll die Templatestruktur aussehen?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 22.06.2025

### Problem: 

Während der gestaltung und implementierung der einzelen Templates stand die Frage, wie die Templates strukturiert werden sollen. Dabei haben wir uns gefragt ob wir für jede einzelene Seite ein eigenes Template schreiben wollen, oder ob wir mit Vererbung arbeiten wollen.

### Unsere Entscheidung: 

Wir haben uns für die Vererbung entscheiden, da wir die base.html nur einmal defineren müssen, und die anderen Templates dann von ihr ereben können. Spezifische Templates wie die der Customer oder Repairer haben dann nochmal ihr eigenes base-Template. Diese base-Template erbt widerum von base.html. Der Hauptgrund für diese Entscheidung ist, dass ansonsten jedes Template einzelt neu geschrieben werden müsste, was die Wartbarkeit und Redudanz deutlich erhöht.

### Mögliche Entscheidungen: 

Wir hatten für den Bereich Templatestrukturierung zwei Optionen: 

+ Templates ohne Vererbung
+ Templates mit Vererbung 
  
| Kriterium | Mit Vererbung | Ohne Vererbung
| :---: | :---: | :---: |
| **Wiederverwendbarkeit** | ✔️Gegeben | ❌Nicht gegeben
|**Wartbarkeit im Code**| ✔️Gering, Zentrale Änderung sind möglich | ❌ Jedes Template muss manuell angepasst werden
|**Skalierbarkeit**| ✔️Bei wachsendem Projekt sehr gut | ❌Bei wachsendem Projekt schwerer
|**Redudanzen**| ✔️Wenig durch Vererbung | ❌Viele Redudanzen im Code

## 06: Gemeinsames User-Modell oder getrennte Rollen in der Datebank?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30.06.2025

### Problem: 

Da in unsere Anwendung zwei Verschieden Nutzerrollen exestieren, müssten wir entscheiden, wie wir diese in der Datenbank modellieren. Die Frage stand dabei, ob es ein gemeinsames User Modell geben soll, oder ob Repairer und Customer getrennt voneinander modelliert werden. Wir haben zunächst Customer und Repairer getrennt voneinander Modelliert. Dabei wurde schnell klar, dass beim Login nicht klar war, welche Rolle sich grade einloggt. Customer und Repairer haben dabei unterschiedliche Funktionen, die nur sie benutzen dürfen. Wir hätten also dann für beide Rollen eine seperate Login-Logik bauen müssen, was deutlich aufwendiger gewesen wäre. Wichtig ist auch noch dass die Repairer Tabelle vorliegen muss, da der Repairer in einer n zu m Beziehung mit Skills steht. 

### Unsere Entscheidung: 

Wir haben uns dafür entschieden eine übergeordnete User-Tabelle zu modellieren, die die ganze Personendaten des Customer und Repairers speichert. Die User-Tabelle steht dann in Beziehung mit Customer und Repairer. Der Vorteil dadurch ist, dass die Login Daten in einer Tabelle exestieren, egal welche Rolle. 

### Mögliche Optionen: 

Für den Bereich der Rollenverteilung in der Datenbank hatten wir drei Optionen: 

+ Customer und Repairer
+ Nur User 
+ User mit Customer und Repairer

| Kriterium | Customer und Repairer | Nur User | User mit Customer und Repairer |
| :---: | :---: | :---: | :--: |
| **Login-Handling** | ❌Seperate Implementierung | ❌Keine Rollenunterscheidung | ✔️Seperater Login möglich
|**Beziehung zu Skills**| ✔️Möglich | ❌Möglich, aber Customer kann auch Skills haben | ✔️Möglich
|**Trennung der Rollen**| ❌Schwer Implementierbar, ohne Normaliserung zu verletzen  | ❌Keine Trennung der Rollen | ✔️Saubere und normaliserte Trennung der Rollen
|**Datenkonsistenz**| ❌Doppelregistrierung einer Email möglich | ❌Unklare Rollenverteilung | ✔️Eindeutig mit User-ID und Fremdschlüssel von Customer oder Repairer


## 07: Braucht man ein Login, um den vollen Funktionsumfang der Website benutzen zu können?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 02.07.2025

### Problem: 

Bei der Ideenfindung, wie wir die Ticketerstellung erstellen wollen sind wir auf das Problem gestoßen, ob Nutzer zwingend eingeloggt sein müssen um Tickets erstellen zu können. Diese Entscheidung betrifft die Benutzerfreundlichkeit sowie Sicherheitsaspekte und Missbrauchpräventionen. Ein zu strenger Login könnte Nutzer oder Erstbesucher der Website abschrecken. 

### Unsere Entscheidung: 

Wir haben uns dafür entschieden, dass man ein Login benötigt, um Tickets erstellen und bearbeiten zu können. Wenn man ohne Login Tickets erstellt und bearbeitet werden Sessions eventuell nicht gespeichert oder führen zu nicht persisteten Sessions, was die Usability deutlich einschränkt. 

### Mögliche Entscheidungen

Wir hatten für den Bereich ob ein Login erforderlich ist zwei Optionen:

+ Login ist erforderlich
+ Login ist nicht erforderlich 

| Kriterium | Login | Kein Login 
| :---: | :---: | :---: |
| **Einfachheit in der Umsetzung** | ✔️Einfach durch Flask-Login(siehe DD NR. 2) | ✔️Einfach
|**Usability**| ✔️Höher durch Registrierung | ❌Gering, aber mehr Fehler schränken Usability ein 
|**Datenkonsistenz**| ✔️Gegeben durch eindeutige Konten | ❌Daten sind nur sessionbasiert
|**Sicherheit**| ✔️Hoch, da nur registrierte Nutzer bestimmte Funktionen nutzen dürfen | ❌Höheres Risiko durch Spam, Fake-Tickets oder falsche Bewertungen



## 08: Wer soll das Ticket als beendet markieren?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 07-07.2025

### Problem: 

Als wir die Ticketfunktion implementiert haben, haben wir uns gefragt wer das Ticket als beendet markieren soll. Dabei stellten sich drei Optionen heraus: Nur der Repairer beendet das Ticket, nur der Customer oder beide Partein. 

### Unsere Entscheidung: 

Wir haben uns dafür entschieden, dass nur der Repairer das Ticket beenden kann, da er die technischen Fähigkeiten hat, zu entscheiden wann der Auftrag als abgeschlossen gilt. Dabei dient der Status der internen Statusverfolgung, nicht der endgültigen Beurteilung. Wenn das Ticket abgeschlossen ist, kann der Customer eine Bewertung zum Ticket schreiben und bei Unzufriedenheiten ein Feedback geben.


### Mögliche Entscheidungen

Wir hatten für den Bereich Ticket-Abschließung drei Optionen:

+ Nur der Repairer
+ Nur der Customer
+ Beide Parteien

| Kriterium | Repairer | Customer | Beide Parteien |
| :---: | :---: | :---: | :--: |
| **Einfachheit in der Umsetzung** | ✔️Einfach | ✔️Einfach | ❌Komplex (Statussynchronisation)
|**Nutzeraufwand**| ✔️Gering | ✔️Gering | ✔️Gering
|**Zuverlässigkeit**| ✔️Repairer schließt in der Regel ab | ❌Customer vergisst es häufiger | ❌Verzögerung durch Customer
|**Missbrauchrisiko**| ✔️Ist da, aber durch Rezension kann gut entgegengewirkt werden | ❌Möglich | ✔️Gering






