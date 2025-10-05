import random
import time


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
    "mir auch danke"
    "gleichfalls",
    "mir geht es auch gut",
    "mir gehts auch gut",
    "super",
    "freut mich",
    "toll"
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


def willkommen():
    print("+++DecisionV0.1+++")
    ladepunkte()
    print("\n+++Das hier wird mal ein kleiner Chatbot mit diversen eingebundenen kleinen Anwendungen+++")
    ladepunkte()
    print("\n+++Zum jetzigen Zeitpunkt kannst du mich grüßen und fragen wie es mir geht.+++")
    ladepunkte()


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

        if user_input == "exit":
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

