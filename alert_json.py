import json
import datetime
import time
import dropbox_file_util

def format_alert(floor, room, body, name, time: str):
    return '{{\"floor\":\"{}\", \"room\":\"{}\",\"body\":\"{}\", \"name\":\"{}\", \"time\":\"{}\"}}'.format(floor, room, body, name, time)

def current_time():
    return datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

'''
formatted_alert = (format_alert(2,228,'water broke', 'Ahsan', '1000'))
print(formatted_alert)
print(json.loads(formatted_alert))

print(str(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')))

dropbox_file_util.Tracker().poll()
'''