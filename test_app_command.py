from core.app_command import handle_app_command

print("ARK Application Test")
print("Type 'exit test' to stop.")

while True:
    command = input("You: ").strip()

    if command.lower() == "exit test":
        break

    if not command:
        continue

    handled = handle_app_command(command)

    if not handled:
        print("ARK: This is not an application-opening command.")