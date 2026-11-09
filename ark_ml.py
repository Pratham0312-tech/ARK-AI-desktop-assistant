
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
import joblib


# ==========================================
# 1. ARK TRAINING DATA
# ==========================================

training_data = {

    "open_app": [
        "open chrome",
        "launch chrome browser",
        "start spotify",
        "open calculator",
        "launch notepad",
        "please open paint",
        "start the calculator application",
        "run microsoft word",
        "launch spotify for me",
        "I want to open notepad",
        "start the chrome application",
        "open my desktop application",
        "open the calculator program",
        "start microsoft excel",
        "launch my music application",
        "run notepad for me",
        "I need to open chrome",
        "please start calculator",
        "open the spotify application",
        "launch paint for me"
    ],

    "open_file": [
        "open my project report",
        "find my python file",
        "open the pdf document",
        "find my resume",
        "open my assignment",
        "locate the text file",
        "show me my presentation file",
        "find the downloaded document",
        "open my project file",
        "search for my notes",
        "can you find my report",
        "I want to open a file",
        "find my excel file",
        "open the document named report",
        "search for my saved pdf",
        "locate my python project file",
        "show me the downloaded file",
        "find my college assignment",
        "open my presentation document",
        "search my computer for a file"
    ],

    "open_folder": [
        "open downloads folder",
        "open documents folder",
        "show me my desktop folder",
        "find my project folder",
        "open the pictures folder",
        "go to downloads folder",
        "open my music folder",
        "find the videos folder",
        "show me my project directory",
        "access my downloads",
        "I want to access the documents folder",
        "take me to the pictures directory",
        "open my desktop directory",
        "show me the downloads directory",
        "go inside my music folder",
        "find the folder named projects",
        "open the folder containing my files",
        "take me to documents",
        "access my project directory",
        "locate the pictures folder"
    ],

    "open_website": [
        "open youtube website",
        "go to google website",
        "open facebook website",
        "visit github website",
        "open instagram website",
        "go to amazon website",
        "visit wikipedia website",
        "open the youtube page",
        "take me to google",
        "open facebook in my browser",
        "visit the website",
        "go to the webpage",
        "open the github webpage",
        "visit youtube in browser",
        "take me to instagram website",
        "open amazon in chrome",
        "go to the google homepage",
        "browse to facebook",
        "visit the wikipedia page",
        "open this URL in browser"
    ],

    "close_app": [
        "close chrome",
        "exit spotify application",
        "quit notepad",
        "stop calculator",
        "close the chrome browser",
        "shut down paint application",
        "please close spotify",
        "terminate chrome browser",
        "I want to close notepad",
        "close microsoft word",
        "quit the calculator application",
        "please exit paint",
        "close the spotify program",
        "shut down microsoft excel",
        "stop the chrome application",
        "I want to quit paint",
        "terminate notepad application",
        "please close the calculator",
        "exit the microsoft word application",
        "close this specific application"
    ],

    "close_all": [
        "close everything",
        "close all applications",
        "shut down all open apps",
        "close every running application",
        "exit all applications",
        "close all programs",
        "I want to close everything",
        "quit all open applications",
        "close all my apps",
        "shut down all programs",
        "please close all applications",
        "close everything that is open",
        "close every application running on my computer",
        "exit all running programs",
        "shut down all my open applications",
        "close all currently running apps",
        "quit every open program",
        "close all software",
        "stop all running applications",
        "I want to close all open apps"
    ],

    "cancel_download": [
        "cancel the download",
        "stop downloading",
        "cancel my current download",
        "stop the file download",
        "abort the download",
        "I want to cancel downloading",
        "stop this download",
        "please cancel the download",
        "cancel the ongoing download",
        "stop downloading the file",
        "abort my current download",
        "cancel all downloads",
        "stop the current file download",
        "cancel the browser download",
        "I don't want this download anymore",
        "abort my ongoing download",
        "stop downloading this file",
        "please stop the download process",
        "cancel the active download",
        "I want to stop this download"
    ],

    "get_time": [
        "what time is it",
        "tell me the time",
        "show current time",
        "what is the time right now",
        "tell me the current time",
        "can you check the time",
        "what time is it now",
        "give me the current time",
        "do you know the time",
        "show me the clock",
        "please tell me the time",
        "current time please",
        "what is the exact time",
        "check the clock for me",
        "tell me what time it is",
        "show the current clock time",
        "can you give me the time",
        "I need to know the time",
        "what time do we have",
        "display the current time"
    ],

    "get_date": [
        "what is today's date",
        "tell me today's date",
        "what date is it",
        "show me the date",
        "what is the current date",
        "tell me the current date",
        "which day is today",
        "what day is it today",
        "give me today's date",
        "can you check the date",
        "show today's date",
        "please tell me the date",
        "what is the date today",
        "display today's date",
        "tell me the day and date",
        "check today's date",
        "I want to know the date",
        "what date are we on",
        "show the current date",
        "can you tell me today's date"
    ],

    "get_datetime": [
        "what is the time and date today",
        "tell me the current time and date",
        "what time and date is it",
        "show today's date and current time",
        "give me both time and date",
        "what is today's date and time",
        "tell me the date and time right now",
        "can you check the time and date",
        "show me the current date and time",
        "what day and time is it",
        "I want to know the time and date",
        "display today's time and date",
        "tell me both the current date and time",
        "what is the time along with today's date",
        "give me today's date and the current time",
        "check what time and date it is",
        "show the clock and today's date",
        "what is the date and time right now",
        "can you tell me both the time and date",
        "I need the current date and time"
    ],

    "exit": [
        "exit ARK",
        "quit ARK",
        "shut down ARK",
        "close ARK assistant",
        "stop ARK",
        "I want to exit ARK",
        "terminate ARK assistant",
        "goodbye ARK",
        "turn off ARK assistant",
        "please shut down ARK",
        "stop the ARK assistant",
        "end the ARK program",
        "I want to close the assistant",
        "please exit the ARK program",
        "turn off ARK",
        "quit the assistant",
        "shut down my ARK assistant",
        "stop the assistant program",
        "end ARK",
        "goodbye assistant"
    ]
}


# ==========================================
# 2. PREPARE SENTENCES AND LABELS
# ==========================================

sentences = []
labels = []

for intent, examples in training_data.items():
    for example in examples:
        sentences.append(example)
        labels.append(intent)

print("Total training examples:", len(sentences))
print("Total intents:", len(training_data))


# ==========================================
# 3. SPLIT TRAINING AND TESTING DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    sentences,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)


# ==========================================
# 4. CONVERT TEXT INTO NUMBERS
# ==========================================

vectorizer = CountVectorizer(
    ngram_range=(1, 2),
    lowercase=True
)

X_train_numbers = vectorizer.fit_transform(X_train)
X_test_numbers = vectorizer.transform(X_test)


# ==========================================
# 5. TRAIN THE ML MODEL
# ==========================================

model = LogisticRegression(
    max_iter=2000,
    class_weight="balanced"
)

model.fit(X_train_numbers, y_train)


# ==========================================
# 6. EVALUATE THE MODEL
# ==========================================

predictions = model.predict(X_test_numbers)

accuracy = accuracy_score(y_test, predictions)

print("\nModel accuracy:", round(accuracy, 2))

print("\nClassification report:")

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# ==========================================
# 7. SHOW INCORRECT PREDICTIONS
# ==========================================

print("\nIncorrect predictions:")

mistake_count = 0

for sentence, actual, predicted in zip(
    X_test,
    y_test,
    predictions
):
    if actual != predicted:
        mistake_count += 1

        print("\nSentence:", sentence)
        print("Correct intent:", actual)
        print("Predicted intent:", predicted)

if mistake_count == 0:
    print("No incorrect predictions!")

print("\nTotal mistakes:", mistake_count)


# ==========================================
# 8. CONFUSION MATRIX
# ==========================================

intent_names = list(training_data.keys())

matrix = confusion_matrix(
    y_test,
    predictions,
    labels=intent_names
)

print("\nConfusion Matrix:")
print("Intent order:", intent_names)
print(matrix)


# ==========================================
# 9. SAVE MODEL AND VECTORIZER
# ==========================================

joblib.dump(
    {
        "model": model,
        "vectorizer": vectorizer
    },
    "ark_ml.pkl"
)

print("\nARK ML model trained and saved successfully!")

print("\nARK can now recognize these intents:")

for intent in training_data:
    print("-", intent)

print("\nTotal training examples:", len(sentences))
