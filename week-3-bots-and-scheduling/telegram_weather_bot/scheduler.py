from apscheduler.schedulers.blocking import BlockingScheduler
import asyncio

def say_hello():
    print("Scheduler is working")
scheduler=BlockingScheduler()
scheduler.add_job(say_hello,trigger='interval',seconds=5)
print("Starting scheduler...")
scheduler.start()