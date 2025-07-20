# Schritte um die App auszuführen 

**Schritt 1:** Installiere ein: [Python Virtual Environment](https://hwrberlin.github.io/fswd/python-vscode.html#32-use-the-python-virtual-environment-as-default-for-this-workspace) 

**Schritt 2:** Installiere alle nötigen requirments mit dem Befehl: `pip install -r requirements.txt`

**Schritt 3:** Damit die Datebank initalisert wird und die Anwendung korrekt funktioniert muss als erstes der Befehl:

`python3 app.py` ausgeführt werden. 

Auf Windows lautet der Befehl: `python app.py`

Im Projektordner muss jetzt der der **instance** Ordner vorliegen. Dieser enthält die SQLite Datebank. 

Nachdem die Datebank zum ersten mal initalisiert wurde reicht der Befehl: `flask run`

Um den Webserver zu schließen muss ins Terminal geklickt werden, wo der Webserver läuft und **COMMAND+C** auf Mac gedrückt werden. Auf Windows schließt man den Webserver mit **STRG+C**.

**Hinweis:** Um unnötige Fehler in Session zu vermeiden, sollten alle Tabs der Anwendung geschloßen werden, bevor man den Webserver beendet. Tut man dies nicht und sendet weiter Anfragen an den Webserver, der schon beendet wurde, kann es zu inkonsistenzen der Session kommen und man bekommt den HTTP-Fehler 403. Dann müsste man alle Cookies löschen, um die Session der Anwednung zu resetten. 














