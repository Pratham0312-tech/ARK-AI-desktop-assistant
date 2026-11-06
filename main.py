from commands import applications
from core.command_processor import is_open_command, is_close_command
import urllib.parse
from commands import system_controls
from utils.voice import listen, speak
import re
from core.app_command import handle_app_command


print("AI Desktop Assistant")
print("Assistant is starting...")
print("hello there i am ark")

# Function to display and speak ARK's responses
def respond(text):
    print("ARK:", text)
    speak(text)


# Choose input mode
print("Choose input mode: type or voice")
mode = input("Mode: ").strip().lower()

if mode in ("voice", "v"):
    speak("Hello, I am ARK. Voice mode is ready.")
    voice_mode = True
else:
    print("Typing mode selected.")
    voice_mode = False 


#loop to run the user input command

while True:
    if voice_mode:
        command = listen()

        if command is None:
            continue
    else:
        command = input("You: ").lower().strip()

    #exit command to break the loop

    if command == "exit":                                                                              
        break

        #separate multiple commands

    tasks = re.split(r"\s+and\s+|\s*,\s*|\s+then\s+", command)
    

    for task in tasks:
        command = task.strip()

        if not command:
            continue

        if command in ("notepad", "calculator", "chrome", "youtube"):
            command = "open " + command

    #date and time conditions

        if "date" in command and "time" in command:
            print("Today's date is:", system_controls.get_current_date())
            print("The current time is:", system_controls.get_current_time())

        elif "yesterday" in command or "yesterdays" in command :
            print("Yesterday's date was:", system_controls.get_relative_date(-1))

        elif "tomorrow" in command or "tomorrows" in command:
            print("Tomorrow's date is:", system_controls.get_relative_date(1))

        elif "today" in command or "date" in command or "todays" in command:
            print("Today's date is:", system_controls.get_relative_date(0))

        elif "time" in command:
                        print("this is the todays time :")
                        print(system_controls.get_current_time())  

        elif handle_app_command(command):
            pass

        #start the open/action section here for apps
        
        elif is_open_command(command):
            parts = command.split()
                
            if "chrome" in command or "google chrome" in command or "chrome browser" in command:
                print("chrome is opening")
                applications.open_chrome()

            elif "notepad" in command or "notepad app" in command or "text editor" in command or "note pad" in command:
                print("opening notepad")
                applications.open_notepad()

            elif "calculator" in command or "calc" in command:
                print("opening calculator")
                applications.open_calculator()

            elif "youtube" in command:
                print("opening youtube")
                applications.open_youtube()


            #File handling section and condition


            elif "open " in command:
                name = " ".join(parts[1:])

                if applications.open_folder(name):
                    print("opening folder", name)

                elif applications.open_file(name):
                    print("opening file", name)

                #website opening condition or searching website by name
                else:
                    url = "https://www.google.com/search?q=" + urllib.parse.quote(name)
                    applications.open_website(url)

                # else part if the command does not match all the loops

            else:
                print("I don't know which application you want to open.")

        elif is_close_command(command):
                    parts = command.split()

                    if len(parts) > 1:
                        app_name = parts[1]
                        print("closing", app_name)
                        applications.close_application(app_name)
                    else:
                        print("Please specify which application to close.")

        else:
            print("Sorry, I don't understand that command yet.")

print("ARK is shutting down.")

    