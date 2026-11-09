
import re
import joblib

from commands.app_discovery import open_app


# Load the trained ML model
saved_data = joblib.load("ark_ml.pkl")

model = saved_data["model"]
vectorizer = saved_data["vectorizer"]


def extract_app_name(command):
    """Remove command words and keep the application name."""

    command = command.lower().strip()

    words_to_remove = [
        "please", "can you", "could you", "would you",
        "ark", "open", "launch", "start", "run",
        "for me", "the application", "the app",
        "application", "app"
    ]

    for word in sorted(words_to_remove, key=len, reverse=True):
        command = re.sub(
            r"\b" + re.escape(word) + r"\b",
            " ",
            command
        )

    return " ".join(command.split()).strip()


def handle_app_command(command):
    """Recognize an app-opening command and open the requested app."""

    command_numbers = vectorizer.transform([command])

    if command_numbers.nnz == 0:
        return False

    prediction = model.predict(command_numbers)[0]

    # Only handle commands classified as open_app
    if prediction != "open_app":
        return False

    # Require an actual app-opening instruction
    if not re.search(r"\b(open|launch|start|run)\b", command.lower()):
        return False

    app_name = extract_app_name(command)

    if not app_name:
        print("ARK: Which application should I open?")
        return True

    print("ARK understood: Open application")
    print("Application requested:", app_name)

    open_app(app_name)

    return True
