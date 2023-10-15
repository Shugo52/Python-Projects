def addtime(start, duration, day=False):
    dayoftheweek = {'monday':0, 'tuesday':1, 'wednesday':2, 'thurday':3, 'friday':4, 'saturday':5, 'sunday':6}
    dayoftheweeklist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    am_or_pm_flip = {'AM':'PM', 'PM':'AM'}
    duration_hour = int(duration.split(':')[0])
    duration_minute = int(duration.split(':')[1])
    start_time = start.split()[0]
    start_hour = int(start_time.split(':')[0])
    start_minute = int(start_time.split(':')[1])
    am_or_pm = start.split()[1]
    end_hour = duration_hour + start_hour
    am_or_pm_flip_counter = int((start_hour + duration_hour))%12
    amount_of_days = int(duration_hour / 24)
    end_minutes = duration_minute + start_minute

    if end_minutes >= 60:
        start_hour += 1
        end_minutes = end_minutes % 60

    if end_minutes > 9:
        end_minutes = end_minutes
    else:
        end_minutes = '0' + str(end_minutes)

    end_hour = (start_hour + duration_hour)%12

    if end_hour == 0:
        end_hour = 12
    else:
        end_hour = end_hour
        
    if am_or_pm == 'PM' and start_hour + (duration_hour%12)>=12:
        amount_of_days += 1

    if (am_or_pm_flip_counter % 2) == 1:
        am_or_pm = am_or_pm_flip[am_or_pm]
    else:
        am_or_pm = am_or_pm
    resulting_time = str(end_hour) + ':' + str(end_minutes)+ ' ' + am_or_pm
    if day:
        day = day.lower()
        index = int((dayoftheweek[day]) + amount_of_days)%7
        resulting_time += ', ' + dayoftheweeklist[index]
    
    

    if amount_of_days == 1:
        resulting_time += '(next day)'
    elif amount_of_days > 1:
        resulting_time += ' (' + str(amount_of_days) + ' days later).' 

    print(resulting_time)
addtime("11:43 AM", "00:20")