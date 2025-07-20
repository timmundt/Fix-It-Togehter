---
title: Chat Routen
parent: Funktionen und Routen
nav_order: 2
---

# Chat Routen

<details open markdown="block">

<summary>Chat Routen</summary>

- [Chat Routen](#chat-routen)
    - [open\_chat(ticket\_id)](#open_chatticket_id)
    - [send\_message()](#send_message)

</details>

### open_chat(ticket_id)

**Route:** /chat/ticket/int:ticket_id 

**Methods:** GET

**Zweck:** Dieser Route ist dafür, für die jeweillige Ticket id den Chat zu öffnen und diesen einsehen zu können, wenn dort schon Nachirchten ausgetauscht wurden. Diese Route wird vom Customer und Repairer benutzt. Dabei werden die Nachirchten vom Customer links angezeigt und die vom Repairer rechts. 

**Möglicher Output:** 

<img src="../../assets/references_assets/open_chat.png" width="600">

### send_message()

**Route:** /chat/send

**Methods:** POST 

**Zweck:** Diese Route ist dafür da um in einem Chat, der geöffnet ist, eine beziehungsweise mehrere Nachirchten senden zu können. Dies geschieht über den Button "Senden". 

<img src="../../assets/references_assets/send_message_1.png" width="600">
<img src="../../assets/references_assets/send_message_2.png" width="600">



