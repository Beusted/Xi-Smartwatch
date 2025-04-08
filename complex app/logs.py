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
    total_steps = 0
    total_distance = 0

    # Convert input date string to datetime object
    input_date = datetime.strptime(date, '%Y%m%d')

    # Find the Monday of the current week
    start_of_week = input_date - timedelta(days=input_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    for key in data:
        current_date = datetime.strptime(key, '%Y%m%d')
        if start_of_week <= current_date <= end_of_week:
            total_steps += data[key]['Total Steps']
            total_distance += data[key]['Distance']

    week_range = f"{start_of_week.strftime('%b %d')} - {end_of_week.strftime('%b %d, %Y')}"
    weekly += f"Week of {week_range}\nTotal Steps: {total_steps}\nTotal Distance: {total_distance} km\n"

    return weekly

