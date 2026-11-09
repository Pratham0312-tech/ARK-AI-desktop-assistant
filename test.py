
import joblib
import re

# Load the trained ML model and vectorizer
saved_data = joblib.load("ark_ml.pkl")

model = saved_data["model"]
vectorizer = saved_data["vectorizer"]

print("ARK ML system is ready!")

while True:
    command = input("You: ").lower().strip()

    # Ignore empty input
    if not command:
        continue

    # Convert the command into numbers
    command_numbers = vectorizer.transform([command])

    # Reject commands containing no known vocabulary
    if command_numbers.nnz == 0:
        print("ARK: Sorry, I don't understand that command.")
        continue

    # Predict the intent
    prediction = model.predict(command_numbers)
    probabilities = model.predict_proba(command_numbers)
    confidence = max(probabilities[0])

    print("Confidence:", round(confidence, 2))

    # Reject low-confidence predictions
    if confidence < 0.40:
        print("ARK: Sorry, I don't understand that command.")
        continue

    intent = prediction[0]

    print("ARK understood the intent:", intent)

    # Extract the application name
    if intent == "open_app":

        words_to_remove = r"\b(open|launch|start|run|the|please|could|you)\b"

        target = re.sub(words_to_remove, "", command)
        target = " ".join(target.split())

        if not target:
            print("ARK: Which application should I open?")
            continue

        print("ARK identified the application:", target)
        print("ARK: I can open an application!")

    elif intent == "get_time":
        print("ARK: I can tell you the time!")

    elif intent == "get_date":
        print("ARK: I can tell you the date!")

    elif intent == "exit":
        print("ARK is shutting down.")
        break
