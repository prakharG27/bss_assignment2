# # fortune.py - Version v1.0


def main():
    print(" Welcome to Prakhar Garg's Fortune Teller (21JE0670) ")
    mood = input("What is your mood today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print(" Fortune: Wonderful opportunities are coming your way, Prakhar! Stay joyful. ")
    elif mood == "sad":
        print(" Fortune: Difficult days will pass, and you will emerge stronger. ")
    elif mood == "neutral":
        print(" Fortune: Serenity brings strength. Enjoy the peace within you. ")
    else:
        print("Apologies, I don't have a fortune for that mood.")

if __name__ == "__main__":
    main()
