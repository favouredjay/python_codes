def seconds_since_midnight(hours, minutes, seconds):
    if hours < 0 or hours > 23:
        raise Exception("Wrong entry")
    else:
        hours = hours * 60*60
        # hours = hour_in_seconds
    if minutes <= 0 or minutes > 60:
        raise Exception("Wrong entry")
    else:
        minutes = minutes * 60
    return hours + minutes + seconds


print(seconds_since_midnight(13, 30, 45))
