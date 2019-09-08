import dropbox
from dropbox.files import WriteMode
import time
import datetime

class Tracker():
    def __init__(self):
        self.dbx = dropbox.Dropbox('8ZGN57lbDHAAAAAAAAAADC9r_ppjXik3EUcGAQvBjxk9dfF3alPkOu83U4_wlEVc')
        alerts_meta = self.dbx.files_list_folder('/TestingFiles/')
        am_len = (len(alerts_meta.entries))
        self.last_len = am_len
        self.alert_folder = '/Alerts/'
        am = (self.dbx.files_list_folder(self.alert_folder))
        self.last_time = am.entries[0].server_modified

    def poll(self):
        #print('Polling')
        alerts_meta = self.dbx.files_list_folder(self.alert_folder)
        am_len = (len(alerts_meta.entries))
        is_new_alert = False
        highest_datetime = self._return_highest_datetime(alerts_meta)
        new_time = alerts_meta.entries[highest_datetime].server_modified
        #print('LN: ', self.last_time, ', ', new_time)
        if self.last_time < new_time:
            is_new_alert = True
        if(am_len == 0):
            is_new_alert = False
        if(is_new_alert):
            self.update_past_data(am_len, new_time)
        return is_new_alert

    def update_past_data(self, cur_len, cur_time):
        self.last_len = cur_len
        self.last_time = cur_time
    def _return_highest_datetime(self, metadata):
        if(len(metadata.entries)==0):
            return None
        if(len(metadata.entries)==1):
            return 0
        latest_index = 0
        for i in range(0, len(metadata.entries)):
            #print(metadata.entries[i].server_modified)
            entry = metadata.entries[i]
            entry_dt = entry.server_modified
            if(entry_dt> metadata.entries[latest_index].server_modified):
                latest_index = i
            #dropbox.files.FileMetadata().server_modified
        #print(latest_index)
        return latest_index

    def pull_last_file(self):
        metadata_list = self.dbx.files_list_folder(self.alert_folder).entries
        metadata = metadata_list[len(metadata_list)-1]
        name = metadata.name
        _,f = self.dbx.files_download(self.alert_folder+name)
        return f.content.decode('utf-8')

    def pull_file(self, index):
        metadata_list = self.dbx.files_list_folder(self.alert_folder).entries
        metadata = metadata_list[index]
        name = metadata.name
        _,f = self.dbx.files_download(self.alert_folder+name)
        return f.content.decode('utf-8')

class Alert_Sender():
    def __init__(self):
        self.dbx = dropbox.Dropbox('8ZGN57lbDHAAAAAAAAAADC9r_ppjXik3EUcGAQvBjxk9dfF3alPkOu83U4_wlEVc')
        self.alerts_folder = '/Alerts/'
    def send_alert(self, alert, alert_time, name):
        self.dbx.files_upload(alert.encode('utf-8'), self.alerts_folder+alert_time + name, mode=WriteMode('add'))