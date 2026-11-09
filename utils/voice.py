
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("ARK:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("ARK is listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower().strip()

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return None

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return None

    except sr.RequestError:
        speak("Speech recognition needs an internet connection.")
        return None

    except OSError as error:
        print("Microphone error:", error)
        return None
