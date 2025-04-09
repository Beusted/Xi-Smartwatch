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

def save_daily_totals(*, filename, date, steps, distance):
    data = read_data(filename=filename)
    data[date] = {
        'Total Steps': steps,
        'Distance': round(distance, 2)
    }
    write_data(data=data, filename=filename)

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

def report_weekly_summary(filename):

    data = read_data(filename=filename)
    if not data:
        return "No data available."

    # Get the latest date in the data
    sorted_dates = sorted(data.keys())
    last_date = sorted_dates[-1]

    # Generate weekly report for the most recent week
    weekly_report = report_weekly(data=data, date=last_date)

    # Calculate averages
    input_date = datetime.strptime(last_date, '%Y%m%d')
    start_of_week = input_date - timedelta(days=input_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    step_sum = 0
    distance_sum = 0.0
    days_count = 0

    for key in sorted_dates:
        current_date = datetime.strptime(key, '%Y%m%d')
        if start_of_week <= current_date <= end_of_week:
            step_sum += data[key]['Total Steps']
            distance_sum += data[key]['Distance']
            days_count += 1

    if days_count == 0:
        return "No data for the past week."

    avg_steps = step_sum / days_count
    avg_distance = distance_sum / days_count

    weekly_report += f"\nAverage Steps per Day: {avg_steps:.2f}\nAverage Distance per Day: {avg_distance:.2f} km\n"

    return weekly_report



