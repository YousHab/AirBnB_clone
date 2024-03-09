#!/usr/bin/env python

from datetime import datetime, date, time

current_time = datetime.now()

#format time

formated_time = current_time.strftime("%Y-%m-%d %H:%M")

print(current_time)

print(formated_time)