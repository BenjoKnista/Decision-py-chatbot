
# 📘 README (Deutsch)

## DecisionV0.1 – Ein einfacher Chatbot in Python

### Beschreibung
Dieses Projekt ist ein kleiner textbasierter Chatbot, der einfache Begrüßungen und Fragen zum Befinden beantworten kann.  
Der Bot erkennt bestimmte Eingaben des Nutzers und reagiert mit zufälligen Antworten aus vordefinierten Listen.  

### Funktionen
- **Begrüßung**: Erkennt Eingaben wie „hi“, „hallo“, „moin“ usw. und antwortet mit einer zufälligen Begrüßung.  
- **Befinden**: Reagiert auf Fragen wie „wie geht es dir?“ oder „alles klar?“ mit passenden Antworten.  
- **Bestätigung**: Erkennt Eingaben wie „super“, „freut mich“ oder „mir auch“ und bestätigt diese.  
- **Fehlerbehandlung**: Gibt Hinweise, wenn die Eingabe nicht verstanden wird. Nach mehreren Fehlversuchen beendet sich das Programm automatisch.  
- **Beenden**: Mit Eingabe von `exit` kann der Chat jederzeit beendet werden.  

### Voraussetzungen
- Python 3.x  
- Keine zusätzlichen Bibliotheken außer den Standardmodulen `random` und `time`.

### Nutzung
1. Starte das Programm mit:
   ```bash
   python chatbot.py
   ```
2. Begrüße den Bot oder frage, wie es ihm geht.  
3. Beende den Chat mit `exit`.  

### Beispiel
```
+++DecisionV0.1+++
...Ladeanimation...
+++Zum jetzigen Zeitpunkt kannst du mich grüßen und fragen wie es mir geht.+++

Du: hallo
Bot: Hi

Du: wie geht es dir
Bot: Mir geht es super, danke der Nachfrage!

Du: exit
Bis zum nächsten mal!
```

---

# 📘 README (English)

## DecisionV0.1 – A Simple Python Chatbot

### Description
This project is a small text‑based german chatbot that can respond to greetings and simple questions about well‑being.  
The bot recognizes specific user inputs and replies with random responses from predefined lists.  

### Features
- **Greeting**: Recognizes inputs like “hi”, “hello”, “moin” and responds with a random greeting.  
- **Well‑being**: Responds to questions like “how are you?” or “everything okay?” with suitable answers.  
- **Confirmation**: Recognizes inputs like “super”, “me too”, or “great” and replies with short confirmations.  
- **Error handling**: Provides hints if the input is not understood. After several failed attempts, the program ends automatically.  
- **Exit**: Type `exit` at any time to quit the chat.  

### Requirements
- Python 3.x  
- No additional libraries required (only `random` and `time` from the standard library).

### Usage
1. Run the program:
   ```bash
   python chatbot.py
   ```
2. Greet the bot or ask how it is doing.  
3. End the chat with `exit`.