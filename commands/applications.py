import webbrowser
import os 
import subprocess

def open_chrome():

    subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


def open_notepad():

    subprocess.Popen(r"C:\Windows\System32\notepad.exe")

def open_calculator():

    subprocess.Popen(r"C:\WINDOWS\system32\calc.exe")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_website(url):
    webbrowser.open(url)

def close_application(app_name):
    subprocess.run(
        ["taskkill", "/F", "/FI", f"IMAGENAME eq {app_name}.exe"],
        capture_output=True
    )

def find_folder(folder_name):
    search_location = os.path.expanduser("~")

    for root, folders, files in os.walk(search_location):
        for folder in folders:
            if folder.lower() == folder_name.lower():
                folder_path = os.path.join(root, folder)
                return folder_path

    return None

def open_folder(folder_name):
    folder_path = find_folder(folder_name)

    if folder_path:
        os.startfile(folder_path)
        return True

    return False    


def find_file(file_name):
        search_location = [os.path.join(os.path.expanduser("~"), "Documents"),
        os.path.join(os.path.expanduser("~"), "Downloads"),
        os.path.join(os.path.expanduser("~"), "Desktop")]

        for search_location in search_location:
            if not os.path.exists(search_location):
                continue


        for root, folders, files in os.walk(search_location):
            for file in files:
                name_without_extension = os.path.splitext(file)[0]

                if (
                    file.lower() == file_name.lower()
                    or name_without_extension.lower() == file_name.lower()
                ):
                    return os.path.join(root, file)

        return None


def open_file(file_name):
    file_path = find_file(file_name)

    if file_path:
        os.startfile(file_path)
        return True

    return False