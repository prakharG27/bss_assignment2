# fortune.py - Version v1.1 

import random

def main():
    print(" Hey there! Welcome to Prakhar Garg's Fortune Teller (21JE0670) ")
    
    mood = input("So, how's your day going? (happy / sad / neutral / stressed): ").strip().lower()

    messages = {
        "happy": [
            "That's awesome to hear, Prakhar! Great things are coming your way ",
            "Keep shining — your happiness is infectious ",
            "Stay joyful! The world needs more of your energy "
        ],
        "sad": [
            "Hey, it's okay to feel down sometimes. You're stronger than you think ",
            "Tough days don’t last, but tough people like you do ",
            "Just a gentle reminder: after the rain comes the rainbow "
        ],
        "neutral": [
            "Feeling balanced, huh? That’s a powerful place to be ",
            "Enjoy the calm — peace is a gift ",
            "Still waters run deep. Keep going, you're doing great "
        ],
        "stressed": [
            "Take a deep breath, Prakhar — you've got this ",
            "One step at a time. You’re doing better than you think ",
            "Pause. Breathe. Restart. You’ll figure it out "
        ]
    }

    if mood in messages:
        print("\n Your fortune: " + random.choice(messages[mood]))
    else:
        print("\n Hmm… I haven’t prepared a fortune for that mood. Try happy, sad, neutral, or stressed!")

if __name__ == "__main__":
    main()
