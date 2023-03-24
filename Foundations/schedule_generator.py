from datetime import datetime
import datetime as dt


# Function
def schedule_generator(days, work_days, rest_days, start_date):
    start_date = start_date
    all_date = []
    work_day = []

    # We add all calendar dates to the list
    for y in range(days):
        calendar_date = start_date + dt.timedelta(days=y)
        all_date.append(calendar_date)

    # We execute the cycle until the length of all_date is equal to 0
    while len(all_date):
        # We copy the processed working days to work_day
        for item in range(work_days):
            work_day.append(all_date[item])
        # We delete from all_date days - working days + weekends of one cycle
        for item in range(work_days + rest_days):
            # Checks if an element exists before deleting it
            if len(all_date) > 0:
                all_date.pop(0)

    print(work_day)


# Function call
schedule_generator(5, 2, 1, datetime(2020, 1, 30))
