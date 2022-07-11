def add_time(start, duration, week=None):

    # Week Days Dictionary
    weekdays = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}

    # Variables of hours, minutes and period (AM or PM)
    temp_period = 'AM'
    hours, mins = start.split(':')
    mins, period = mins.split(' ')
    duration_hours, duration_mins = duration.split(':')

    # Set a temporary variable of hours
    tmp_hours = (int(hours) + int(duration_hours))

    if period == 'PM':
        tmp_hours += 12

    # Set a temporary variable of minutes
    tmp_mins = (int(mins) + int(duration_mins))

    if(tmp_mins > 59):
        tmp_hours += 1
    
    # Number of days passed after the duration
    days = int(tmp_hours//24) 

    output_hours = tmp_hours % 24
    output_mins = tmp_mins % 60
  
    if output_hours > 11:
        temp_period = 'PM'

    # Convert to 12h
    if output_hours > 12:
        output_hours -= 12
    elif output_hours == 0:
        output_hours = 12

    # The final output
    new_time = str(output_hours) + ":"
    new_time += str(output_mins).zfill(2) + f" {temp_period}"
  
    # If user put a week day, run the code beneath
    if week != None:
        week = week.lower()
        week_num = weekdays[week]
        new_week_num = (days + week_num) % 7
      
        new_week = list(weekdays.keys())[list(weekdays.values()).index(new_week_num)]
        new_time += ', ' + new_week.capitalize()
    
    if days > 1:
        new_time += ' (' + str(days) + ' days later)'
    elif days > 0:
        new_time += ' (next day)'

    return new_time