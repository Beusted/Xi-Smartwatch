import json
import calendar
from datetime import datetime, timedelta

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
    for key in sorted(data.keys()):
        month = calendar.month_name[int(key[4:6])]
        day = f'{month} {int(key[6:8])}, {key[0:4]}'
        steps = data[key]['Total Steps']
        distance = data[key]['Distance']
        daily += f'{day:<20} Steps: {steps:<6} Distance: {distance} km\n'

    return daily

def report_weekly(*, data, date):
    weekly = ''
    total_steps = 0
    total_distance = 0.0

    input_date = datetime.strptime(date, '%Y%m%d')
    start_of_week = input_date - timedelta(days=input_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    for key in sorted(data.keys()):
        current_date = datetime.strptime(key, '%Y%m%d')
        if start_of_week <= current_date <= end_of_week:
            total_steps += data[key]['Total Steps']
            total_distance += data[key]['Distance']

    week_range = f"{start_of_week.strftime('%b %d')} - {end_of_week.strftime('%b %d, %Y')}"
    weekly += f"Week of {week_range}\nTotal Steps: {total_steps}\nTotal Distance: {total_distance:.2f} km\n"

    return weekly


