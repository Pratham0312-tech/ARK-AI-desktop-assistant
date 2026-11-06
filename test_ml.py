
import joblib

# Load the trained ARK model
saved_data = joblib.load("ark_ml.pkl")

model = saved_data["model"]
vectorizer = saved_data["vectorizer"]

print("ARK ML command testing")
print("Type 'exit test' to stop.\n")

while True:

    command = input("You: ").strip()

    if command.lower() == "exit test":
        print("Testing finished.")
        break

    if not command:
        continue

    # Convert the command into numbers
    command_numbers = vectorizer.transform([command])

    # Check whether the model recognizes any words
    if command_numbers.nnz == 0:
        print("ARK: I don't recognize this command.\n")
        continue

    # Predict the intent
    prediction = model.predict(command_numbers)[0]

    # Calculate confidence estimate
    probabilities = model.predict_proba(command_numbers)[0]
    confidence = max(probabilities)

    print("Predicted intent:", prediction)
    print("Confidence:", round(confidence * 100, 2), "%")
    print()
