import time, subprocess
from datetime import datetime as dt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from application.models import db, LogDB, RecordDB
from application import create_app

app = create_app() 

def get_last_n_records(f="/var/log/icecast/song-history.log", n=2):
    proc = subprocess.Popen(['tail', f'-n {n}', f], stdout=subprocess.PIPE)
    lines = proc.stdout.readlines()
    return lines[-1].decode().strip()


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.event_type == "modified" and event.src_path == "/var/log/icecast/song-history.log":
            with app.app_context():
                try:                
                    last_record = get_last_n_records()
                    song = LogDB(time=dt.now(), message=last_record)
                    db.session.add(song)
                    db.session.commit()
                except Exception as e:
                    print(e)


def notify():
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/var/log/icecast', recursive=False)
    observer.start()
    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()