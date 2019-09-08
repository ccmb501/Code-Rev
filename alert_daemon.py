import threading
import time
import alert_json
import dropbox_file_util
'''
def print_work_a():
    print('Starting thread: ', threading.current_thread().name)
    time.sleep(2)
    print('Wrap it up, ', threading.current_thread().name)

def print_work_b():
    print('Starting of thread: ', threading.current_thread().name)
    print('Wrap it up, ', threading.current_thread().name)

a = threading.Thread(target=print_work_a, name='Thread-a')
b = threading.Thread(target=print_work_b, name='Thread-b')

a.start()
b.start()
'''
send_period = 10
alerts_to_send = 3

'''
os = dropbox_file_util.Alert_Sender()
alert_time = alert_json.current_time()
alert = alert_json.format_alert(0, '025', 'water slapped', 'Spiderman', alert_time)
name = 'Spiderman'
os.send_alert(alert, alert_time, name)
'''

'''

#Just a way for how to recieve and show notifications

def alert_sender():
    os = dropbox_file_util.Alert_Sender()
    for i in range(0, alerts_to_send):
        alert_time = alert_json.current_time()
        alert = alert_json.format_alert(0, '025', 'water slapped', 'Spiderman', alert_time)
        name = 'Spiderman'
        os.send_alert(alert, alert_time, name)
        time.sleep(send_period)

def alert_tracker():
    print('Tracking Alerts')
    tracker = dropbox_file_util.Tracker()
    #Check x times
    checks = 30
    update_period = 1
    for i in range(0, checks):
        #print('Polling')
        is_alert = tracker.poll()
        if(is_alert):
            alert = tracker.pull_last_file()
            print('There is an alert: ', alert)
        time.sleep(update_period)

#t = dropbox_file_util.Tracker()
#print(t.pull_first_file())

a = threading.Thread(target=alert_sender, name='Thread-a')
b = threading.Thread(target=alert_tracker, name='Thread-b')

a.start()
b.start()
'''