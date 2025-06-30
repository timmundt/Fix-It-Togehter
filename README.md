# Generally 

This repository is a project work at the HWR Berlin in the module full stack development. Our idea is a platform-based website where people with broken coffee machines and people that can fix broken coffee machines can connect together. The repository includes our source code and the documentation of our project.

Git Basics:

Auf welcher Branch bin ich?

`git branch`

Branch erstellen:

`git branch -b checkout branchname`

Branch zum erstenmal auf Github pushen: 

`git push -u origin branchname`

Branch wechseln:

`git checkout branch-name`

Neues Branch starten:

`git checkout main`

`git pull origin main`

`git checkout -b branchname`

`git push -u origin branchname`

Merge vorbereiten(commit und push auf aktueller Branch nicht vergessen!):

`git checkout main`

`git pull origin main` 

`git checkout branchname-der-gemergert-weden-soll`

`git merge main #Eventuelle Konflike lösen`

Wichtig:
Immer vor dem pushen die main pullen!!!!!!

Commits im Präsenz schreiben!

Keine Konflikte ignorieren!

# Steps to execute the app 

**Step 1:** set up a [Python Virtual Environment](https://hwrberlin.github.io/fswd/python-vscode.html#32-use-the-python-virtual-environment-as-default-for-this-workspace) 

**Step 2:** Install all necessary requirments via this command: `pip install -r requirements.txt`

**Important:** Your terminal should be look like this: 

On unix based distrubution systems: 

```console
venvtimmundt@MacBook-Pro webapp 
```

On windows: 

```console
(venv) 
````

Important is venv at the front!

**Step 3:** 

To initialize the database u must run the following command: 

```console
python3 app.py
```

If u only exectue `flask run` the database will not be initialized and the app is not working in a correct way.













