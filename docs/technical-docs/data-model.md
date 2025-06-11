---
title: Data Model
parent: Technical Docs
nav_order: 2
---

Für die Realisierung unsere Projektes brauchen laut jetztigen Stand 3 Tabellen, eine Tabelle für die Customer, eine Tabelle für die Repairer und eine Tabelle für die Tickets. Diese sehen wie folgt aus: 

## Customer 

Customer(#customer_id,name,vorname,email,passwort,ort)

## Repairer

Repairer(#repairer_id,name,vorname,email,passwort,ort,Firma_X, Firma_Y, Firma_Z ...)

Wichtig: Wir haben es uns beim Repairer so gedacht, dass der Repairer in seinem Konto Profil hinterlegt, welche Firma er reparieren kann. Dass wird dann in dieser Tabelle entsprechend mit true oder false gespeichert.

## Ticket

ticket(#ticket_id,<FK>customer_id,<FK>repairer_id,accepted)

