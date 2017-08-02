import os, logging
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from uber import get_tracking_data
from uber_mongo import add_track

def track():
    print('Populating new data')
    print(datetime.utcnow())
    add_track(get_tracking_data('home', 'office'))
    add_track(get_tracking_data('office', 'home'))

if __name__ == '__main__':
    # for apscheduler
    logging.basicConfig()

    scheduler = BlockingScheduler()
    scheduler.add_job(track, 'cron', year='*', month='*', day='*', week='*', day_of_week='*', hour='*', minute='0,12,20,30,40,50', second=0)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
