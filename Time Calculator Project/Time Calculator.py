def add_time(start_time, duration, start_day=None):
    # Parsing start time
    start_time, period = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if period == 'PM':
        start_hour += 12

    # Parsing duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Total duration in minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # New time
    new_hour = (start_hour + duration_hour + (start_minute + duration_minute) // 60) % 24
    new_minute = (start_minute + duration_minute) % 60

    # Determining days later
    days_later = total_minutes // (24 * 60)
    day_suffix = ''
    if days_later == 1:
        day_suffix = ' (next day)'
    elif days_later > 1:
        day_suffix = f' ({days_later} days later)'

    # Converting new time to 12-hour format
    new_period = 'PM' if new_hour >= 12 else 'AM'
    if new_hour >= 12:
        new_hour -= 12
    if new_hour == 0:
        new_hour = 12

    # Get day of the week if start_day is provided
    if start_day:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = weekdays.index(start_day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        day_of_week = f', {weekdays[new_day_index]}'
    else:
        day_of_week = ''

    # Construct result string
    # Remove leading zero from hour part if it exists
    new_hour_formatted = new_hour if new_hour > 9 else new_hour % 10
    new_time = f'{new_hour_formatted}:{new_minute:02d} {new_period}{day_of_week}{day_suffix}'

    return new_time

# Test cases
print(add_time('3:30 PM', '2:12'))  
print(add_time('11:55 AM', '3:12')) 
print(add_time('8:16 PM', '466:02')) 
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05'))
print(add_time('3:30 PM', '2:12', 'Monday'))
