def is_open_command(command):
    command = command.lower().strip()
    return command.startswith(("open ", "launch ", "start ", "run "))


def is_close_command(command):
    command = command.lower().strip()
    return command.startswith(("close ", "stop ", "quit ", "exit "))