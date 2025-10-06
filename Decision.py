import random
import time
import winsound
import datetime


user_datum_uhrzeit = [
    "datum",
    "uhrzeit"
]

user_begruessung = [
    "hi", "hallo", "moin", "moinsen", "servus", "guten tag", "tag"
]

bot_begruessung = [
    "Hi", "Hallo", "Moin", "Moinsen","Guten Tag"
]

user_ergehen_fragen = [
    "wie geht es dir",
    "wie gehts dir",
    "wie gehts",
    "alles klar",
    "alles fit",
    "wie läufts",
    "wie geht es",
    "gehts dir gut",
    "na alles gut",
    "wie fühlst du dich",
    "was geht"
]

user_bestaetigung = [
    "auch",
    "mir auch",
    "mir auch danke",
    "auch danke",
    "gleichfalls",
    "mir geht es auch gut",
    "mir gehts auch gut",
    "super",
    "freut mich",
    "toll"
]

user_beenden = [
    "exit",
    "beenden",
    "close",
    "tschüss"
]

bot_ergehen = [
    "Mir geht es super, danke der Nachfrage!",
    "Alles bestens bei mir. Und bei dir?",
    "Ich kann mich nicht beklagen – läuft!",
    "Danke, mir geht’s gut. Wie sieht’s bei dir aus?",
    "Alles im grünen Bereich!",
    "Mir geht’s prima, danke. Und dir?",
    "Ich bin voller Energie – was geht bei dir?"
]

bot_besteatigung = [
    "Prima!",
    "Super!",
    "Sehr gut!",
    "Top!",
    "Alles easy!"
]


def ladepunkte():
    laden = "."
    time.sleep(0.5)
    print(laden, end="")
    time.sleep(0.5)
    print(laden, end="")
    time.sleep(0.5)
    print(laden, end="")
    time.sleep(0.5)
    print(laden, end="")
    time.sleep(0.5)


#def melodie():                              #Platzhalter // Soon
    #winsound.Beep(587, 400)
    #winsound.Beep(784, 500)


def willkommen():
    winsound.Beep(784, 500)
    print("+++DecisionV0.2+++")
    ladepunkte()
    print("\n+++Das hier wird mal ein kleiner Chatbot mit diversen eingebundenen kleinen Anwendungen+++")
    ladepunkte()
    hauptmenue()
    return


def hauptmenue():
    winsound.Beep(650, 500)
    print("\n" * 100)
    print("+++DecisionV0.2+++")
    print("+++Hauptmenü+++")
    ladepunkte()
    print("\n1. Hilfe")
    print("2. Datum/Uhrzeit anzeigen")
    return


def hilfe():
    ladepunkte()
    print("\n+++Hilfe+++")
    print("+++Hier findest du eine kleine Anleitung+++")
    print("\n+++Du kannst den Bot einfach grüßen mit: Hi, Hallo, Moin, Moinsen, Servus, Guten Tag, Tag+++")
    print("+++Um Gespräche führen zu können, kannst du einfach fragen: Wie gehts?, Wie gehts dir?, Was geht?, Alles klar? o.ä.+++")
    print("+++Um Funktionen nutzen zu können, kannst du folgende Stichworte in die Konsole eintippen+++")
    ladepunkte()
    print("\nDatum oder Uhrzeit ------------> Zeigt dir immer das aktuelle Datum und die Uhrzeit gleichzeitig")
    print("Hauptmenü ---------------------> So gelangst du von überall in das Hauptmenü zurück")
    print("Exit, Close, Tschüss, Beenden -> Schließt die Anwendung sofort")
    return



def datum_uhrzeit():
    antwort_datum_uhrzeit = datetime.datetime.now()
    return antwort_datum_uhrzeit


def begruessung():
    antwort_begruessung = bot_begruessung
    return random.choice(antwort_begruessung)


def ergehen():
    antwort_ergehen = bot_ergehen
    return random.choice(antwort_ergehen)


def bestaetigung():
    antwort_bestaetigung = bot_besteatigung
    return random.choice(antwort_bestaetigung)


def main():
    fehler_zaehler = 0

    while True:
        user_input = input("\nDu: ").lower()

        if any(wort == user_input for wort in user_beenden):
            print("\nBis zum nächsten mal!")
            ladepunkte()
            break

        if any(wort == user_input for wort in user_begruessung):
            print(begruessung())
            fehler_zaehler = 0
        elif any(wort in user_input for wort in user_ergehen_fragen):
            print(ergehen())
            fehler_zaehler = 0
        elif any(wort == user_input for wort in user_bestaetigung):
            print(bestaetigung())
            fehler_zaehler = 0
        elif any(wort in user_input for wort in user_datum_uhrzeit):
            print("Gerne! Hier hast du das aktuelle Datum und die Uhrzeit:\n")
            print(datum_uhrzeit())
            fehler_zaehler = 0
        elif user_input == "hilfe":
            hilfe()
            fehler_zaehler = 0
        elif user_input == "1":
            hilfe()
            fehler_zaehler = 0
        elif user_input == "hauptmenü":
            hauptmenue()
            fehler_zaehler = 0

        else:
            fehler_zaehler = fehler_zaehler + 1
            if fehler_zaehler == 1:
                print("Irgendwas läuft hier schief, probiers gerne nochmal!")
            elif fehler_zaehler == 2:
                print("Hey das war jetzt schon der zweite Versuch.")
            elif fehler_zaehler == 3:
                print("Ok so langsam solltest du dich entscheiden...")
            else:
                print("Das waren leider zu viele Fehlversuche. Ich muss dann mal los. Versuch es gerne später nochmal!")
                return


willkommen()
main()

