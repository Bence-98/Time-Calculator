def add_time(start, duration, starting_day=""):

  days = [
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
    "sunday"
  ]

  time_full = start.split()
  time = time_full[0].split(":")
  if time_full[1] == "AM":
    ampm = True
  else:
    ampm = False
  duration = duration.split(":")
  plus_days = 0
  time[0] = int(time[0])
  time[1] = int(time[1])
  duration[0] = int(duration[0])
  duration[1] = int(duration[1])
  time[0] += duration[0]
  time[1] += duration[1]
  while time[0] > 12:
    time[0] = time[0] - 12
    if ampm == False:
      plus_days += 1
    ampm = not ampm
  if time[1] > 60:
    time[0] += 1
    time[1] -= 60
    if time[0] >= 12:
      if ampm == False:
        plus_days += 1
      ampm = not ampm
  if starting_day != "":
    starting_day = starting_day.lower()
    starting_day = days.index(starting_day)
    starting_day += plus_days
    while starting_day > 6:
      starting_day -= 7
  else:
    starting_day = ""
  if ampm == True:
    ampm = "AM"
  else:
    ampm = "PM"
  if starting_day != "":
    new_day = ", " + days[starting_day].capitalize()
  else:
    new_day = ""
  if plus_days == 0:
    days_later = ""
  elif plus_days == 1:
    days_later = " (next day)"
  else:
    days_later = " (" + str(plus_days) + " days later)"
  if time[1] < 10:
    time[1] = "0" + str(time[1])
  new_time = str(time[0]) + ":" + str(
    time[1]) + " " + ampm + new_day + days_later
  return new_time