from plyer import notification
import json

def send_notification(alert: str):
    data = json.loads(alert)
    notification.notify(title='Code Rev Emergency: Room '+ data[1], message=data[2] + '- '+data[3], app_name='coderev',timeout=20)