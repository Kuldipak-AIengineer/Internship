from apscheduler.schedulers.background import BackgroundScheduler
from fetch_data import fetch_new_info

# Start the background scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_new_info, 'interval', hours=1)
scheduler.start()

# Keep the script running to allow background scheduler to work
if __name__ == "__main__":
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
