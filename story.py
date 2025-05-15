def start():
    print("\nYou wake up in the Mojave Desert. The sky is pink. A strange signal hums in the distance.")
    print("What do you do?")
    print("1. Walk toward the signal")
    print("2. Stay and wait")
    print("3. Try to remember how you got here")
    choice = input("> ")

    if choice == "1":
        go_to_signal()
    elif choice == "2":
        stay_put()
    elif choice == "3":
        remember()
    else:
        print("Invalid choice.")
        start()

def go_to_signal():
    print("\nThe hum becomes louder. A drone appears overhead with a blinking light.")
    print("1. Wave at it")
    print("2. Run for cover")
    choice = input("> ")

    if choice == "1":
        print("\nThe drone scans you and drops a metal sphere. Your story begins...")
    elif choice == "2":
        print("\nYou find shelter in a rusted-out van. Inside is a map with your name on it...")
    else:
        go_to_signal()

def stay_put():
    print("\nHours pass. The sun rises. You feel thirsty and disoriented.")
    print("1. Look for water")
    print("2. Meditate")
    choice = input("> ")

    if choice == "1":
        print("\nYou stumble upon a dry well... but something glints at the bottom.")
    elif choice == "2":
        print("\nYou fall into a trance and receive a vision: a girl named Miranda running through sand.")
    else:
        stay_put()

def remember():
    print("\nYou try to remember your face before your parents were born.")
    print("1. Mu")
    print("2. Meditate")
    choice = input("> ")

    if choice == "1":
        print("\nYou feel the sound o mu vibrating in your bones.")
    elif choice == "2":
        print("\nYou count your breaths and feel a connection to the universe.")
    else:
        stay_put()
# Start the story
start()
