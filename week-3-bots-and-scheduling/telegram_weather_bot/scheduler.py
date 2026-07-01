from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

async def say_hello():
    print("Scheduler is working")
scheduler=AsyncIOScheduler()
scheduler.add_job(say_hello,trigger='interval',seconds=3)
print("Starting scheduler...")
async def main():
    scheduler.start()
    while True:
        await asyncio.sleep(1)
if __name__=="__main__":
    asyncio.run(main())