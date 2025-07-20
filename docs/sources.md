---
title: Quellen
nav_order: 99
---

# Projekt Dokumentation

## _config.yml 

Quelle: https://github.com/hwrberlin/fswd-app/blob/main/docs/_config.yml

## Allgemeine Struktur

An der gesamten Struktur des docs folder wurde sich am folgendene Repo orientiert:
https://github.com/hwrberlin/fswd-app/tree/main/docs



## Startseitenelemente und Quellen:

Bildquelle: https://g.co/gemini/share/71884990dc25 zuletzt aufgerufen am: 03.07.2025
Promopt: Kannst du ein photolealistisches Bild von einer De'Longhi Kaffemaschine auf einer Werkbank generieren?


Icon-Quellen: https://icons.getbootstrap.com/ zuletzt aufgerufen am: 03.07.2025

## Quellenübersicht für die jeweiligen Templates:

| Template                         | Quelle                                                                 | Funktion                                                                                   |
|:--------------------------------|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| `imprint.html`                  | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Impressum anzeigen                                                                         |
| `index.html`                    | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Startseite                                                                                 |
| `privacy_policy.html`          | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Datenschutzrichtlinie anzeigen                                                             |
| `terms_of_use.html`            | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Nutzungsbedingungen anzeigen                                                               |
| `login.html`                   | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Login-Seite für Nutzer:innen                                                               |
| `register.html`                | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Registrierung neuer Nutzer:innen                                                           |
| `customer_base.html`           | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Kunden-Dashboard / Navigation                                                              |
| `get_tickets.html`             | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Übersicht aller Tickets des Kunden                                                         |
| `ticket_confirmation.html`     | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Bestätigungsseite mit Zusammenfassung des erstellten Tickets                               |
| `ticket_step1_model.html`      | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Schritt 1: Auswahl des Gerätemodells                                                       |
| `ticket_step2_init_message.html` | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Schritt 2: Beschreibung des Problems                                                       |
| `ticket_step3_repairer.html`   | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Schritt 3: Auswahl der passenden Reparateur:in basierend auf Fähigkeiten und Bewertungen   |
| `ticket_step3_repairer.html`   | [Link](https://chatgpt.com/share/687cc85e-8760-8005-a71a-6fdb9f03e4e6) | Sortierung nach Bewertung (high/low)                                                       |
| `ticket_step3_repairer.html`   | [Link](https://chatgpt.com/share/687cc85e-8760-8005-a71a-6fdb9f03e4e6) | Reparateurauswahl mit Rezension-Einsicht basierend auf Modell                              |
| `submit_review.html`        | [Link](https://chatgpt.com/share/687be667-3568-8005-9ebd-c42d425b8360) | Erstellung und Speicherung von Rezensionen durch Kund:innen                                  |
| `repairer_reviews.html`          | [Link](https://chatgpt.com/share/687cc85e-8760-8005-a71a-6fdb9f03e4e6) | Anzeige der Reparateur-Rezensionen mit Sternen und – falls vorhanden – Kommentar           |
| `get_tickets.html`              | [Link](https://chatgpt.com/share/687be667-3568-8005-9ebd-c42d425b8360) | Anzeige bereits abgegebener Rezensionen zu vergangenen Tickets                                       |
| `customer_base.html`            | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Navigation (Sidenav) – basiert auf Vorlage, wurde jedoch angepasst                                   |
| `base.html`                     | [Link](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Clickbarer Footer mit Links zu Impressum, Datenschutz, Nutzungsbedingungen usw.                     |


## Quellenübersicht für das Routing:

| Route                          | Methoden     | Funktion im Code            | Template                         | Quelle                                                                 | Beschreibung                                                                 |
|-------------------------------|--------------|-----------------------------|----------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `/ticket/step1`               | GET, POST    | `ticket_step1()`            | `ticket_step1_model.html`        | [ChatGPT](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Auswahl eines Gerätemodells, Speichern in Session                            |
| `/ticket/step2`               | GET, POST    | `ticket_step2()`            | `ticket_step2_init_message.html` | [ChatGPT](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Eingabe einer Fehlerbeschreibung, Ergänzung der Session                      |
| `/ticket/step3`               | GET, POST    | `ticket_step3()`            | `ticket_step3_repairer.html`     | [ChatGPT](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Verwaltung der Session-Daten, Navigation zur Reparateurauswahl               |
| `/ticket/step3`               | GET, POST    | `ticket_step3()`            | `ticket_step3_repairer.html`     | [ChatGPT](https://chatgpt.com/share/687cc85e-8760-8005-a71a-6fdb9f03e4e6) | Auswahl Reparateur:in, Anzeige der Rezensionen, Sortierung nach Bewertung    |
| `/ticket-bestätigung`        | GET, POST    | `ticket_confirmation()`     | `ticket_confirmation.html`       | [ChatGPT](https://chatgpt.com/share/6866576f-daf8-8005-86b5-a1c42e29fb28) | Zusammenfassung & finale Ticketerstellung, Speichern in DB                   |
| `/get-tickets`               | GET          | `get_tickets()`             | `get_tickets.html`               | [ChatGPT] (hier einfügen link) | hier einfügen  |
| `/account-information`       | GET, POST    | `get_account_info()`        | `customer_account.html`          | [ChatGPT] (hier einfügen link)                                                                     | Anzeige und Bearbeitung der Accountdaten, inkl. Passwortänderung             |


## Screenshots der Quellen:

[Screenshots von D.G Link](https://drive.google.com/drive/folders/1yaMuLX8WIxFJhwy6uMOENw6PvbHgQn-J?usp=drive_link)




