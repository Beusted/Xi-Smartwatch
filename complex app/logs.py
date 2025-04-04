import json
import calendar

def read_data(*, filename):
    try:
        with open(filename, 'r') as openfile:
            x = json.load(openfile)
            return(x)
    except FileNotFoundError:
        return({})
    
def write_data(*, data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def report_daily(*, data, date):
    daily = ''
    day = ''
    steps = 0
    distance = 0

    for key in data:
        month = calendar.month_name[int(key[4:6])]
        day = (f'{month} {key[6:8]}, {key[0:4]}')
        steps = data[key]['Total Steps']
        distance = data[key]['Distance']
        daily = daily + (f'{day:<20} {steps} {distance}')

    return(daily)

def report_weekly(*, data, date):
    weekly = ''
    days = ''
    total_steps = 0
    total_distance = 0

    for key in data:
        month = calendar.month_name[int(key[4:6])]
        #days = (f'{month} {key[6:8]}, {key[0:4]}')
        #steps = data[key]['Total Steps']
        #distance = data[key]['Distance']
        #weekly = weekly + (f'{day:<20} {steps} {distance}')

    return(weekly)

