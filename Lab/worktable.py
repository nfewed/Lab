import datetime

def worktable(days, work_days, rest_days, start_date):
    day = 86400 # 1 day represented in seconds
    worktable = [start_date] # List of workdays
    
    for i in range(days): # We are creating work table with restdays
        worktable.append(datetime.datetime.fromtimestamp(start_date.timestamp() + i*day))
    
    i = work_days
    removedItems = 0
    while i < days: # In this loop we remove restdays from work table
        j = 0
        while j < rest_days:
            worktable.pop(i + j - removedItems)
            removedItems += 1
            j += 1
        i += work_days + j
    
    return worktable

print(worktable(5, 2, 1, datetime.datetime(2020, 1, 30)))