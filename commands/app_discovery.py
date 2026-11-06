
import os
import subprocess
import json
from pathlib import Path
from difflib import SequenceMatcher


def get_start_menu_apps():
    """Discover apps from Windows Start Menu shortcuts."""
    apps = {}

    start_menu_locations = [
        Path(os.environ.get("APPDATA", "")) /
        "Microsoft/Windows/Start Menu/Programs",

        Path(os.environ.get("PROGRAMDATA", "")) /
        "Microsoft/Windows/Start Menu/Programs"
    ]

    for location in start_menu_locations:
        if not location.exists():
            continue

        for root, folders, files in os.walk(location):
            for filename in files:
                if filename.lower().endswith(".lnk"):
                    name = Path(filename).stem
                    path = Path(root) / filename

                    apps[name.lower()] = {
                        "name": name,
                        "type": "shortcut",
                        "target": str(path)
                    }

    return apps


def get_windows_start_apps():
    """Discover registered Windows apps, including many system apps."""
    apps = {}

    try:
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-StartApps | Select-Object Name, AppID | ConvertTo-Json -Compress"
            ],
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode != 0 or not result.stdout.strip():
            return apps

        data = json.loads(result.stdout)

        if isinstance(data, dict):
            data = [data]

        for app in data:
            name = app.get("Name")
            app_id = app.get("AppID")

            if name and app_id:
                apps[name.lower()] = {
                    "name": name,
                    "type": "start_app",
                    "target": app_id
                }

    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError) as error:
        print("Windows app discovery warning:", error)

    return apps


def discover_apps():
    """Combine apps found in both Windows locations."""
    apps = get_start_menu_apps()
    apps.update(get_windows_start_apps())
    return apps


def find_app(app_name):
    """Find an installed app by its name."""
    apps = discover_apps()
    requested = app_name.lower().strip()

    if not requested:
        return None

    # Exact match
    if requested in apps:
        return apps[requested]

    # Match when the requested name is contained in one app name
    partial_matches = [
        app for key, app in apps.items()
        if requested in key or key in requested
    ]

    if len(partial_matches) == 1:
        return partial_matches[0]

    if len(partial_matches) > 1:
        print("ARK: I found multiple matching applications:")
        for app in partial_matches[:10]:
            print("-", app["name"])
        return None

    # Fuzzy matching for small spelling differences
    scores = []

    for key, app in apps.items():
        score = SequenceMatcher(None, requested, key).ratio()
        scores.append((score, app))

    scores.sort(key=lambda item: item[0], reverse=True)

    if not scores or scores[0][0] < 0.78:
        return None

    if len(scores) > 1 and scores[0][0] - scores[1][0] < 0.08:
        print("ARK: I found multiple possible applications:")
        for score, app in scores[:5]:
            print("-", app["name"])
        return None

    return scores[0][1]


def open_app(app_name):
    """Open a discovered Windows application."""
    app = find_app(app_name)

    if not app:
        print(f"ARK: I could not find the application '{app_name}'.")
        return False

    try:
        if app["type"] == "shortcut":
            os.startfile(app["target"])

        elif app["type"] == "start_app":
            subprocess.Popen([
                "explorer.exe",
                "shell:AppsFolder\\" + app["target"]
            ])

        print(f"ARK: Opening {app['name']}.")
        return True

    except OSError as error:
        print("ARK: Could not open the application:", error)
        return False


if __name__ == "__main__":
    print("ARK - Windows Application Discovery Test")
    print("----------------------------------------")

    apps = discover_apps()
    print(f"Discovered {len(apps)} applications.\n")

    app_name = input("Enter an application name to open: ").strip()

    if app_name:
        open_app(app_name)
