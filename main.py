import time
import pyttsx3
import random

def main():
    
    # Read responses from file and add to array
    responses = []
    with open("Responses.txt", "r") as txt_file:
        for line in txt_file:
            responses.append(line)

    # initiates text to speech engine
    engine = pyttsx3.init()
    while True:
        # five minutes == 300 seconds
        FIVE = 300
        totalTime = 0

        # timer to count out five minutes
        while totalTime != FIVE:
            time.sleep(1)
            totalTime += 1
            print(totalTime, end='\r', flush=True)

        # Prints posture check message and says said message
        rand = random.choice(responses)
        print(f'\n{rand}\n')
        engine.say(rand)
        engine.runAndWait()

if __name__ == '__main__':
    main()