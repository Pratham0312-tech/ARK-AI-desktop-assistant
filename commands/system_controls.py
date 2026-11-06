from datetime import datetime,timedelta

def get_current_time():
    current =datetime.now()
    return current.strftime("%I:%M %p")


def get_current_date():
    date = datetime.now()
    return date.strftime("%d/%B/%Y")

def get_relative_date(days):
    current = datetime.now()
    new_date = current + timedelta(days=days)
    return new_date.strftime("%d %B %Y")