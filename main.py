import os
import sys

import schedule
import time
from OpenAIAuth import Auth0


def job():
    auth = Auth0(email_address=sys.argv[1], password=sys.argv[2])
    access_token = auth.get_access_token()
    os.system("docker stop chatgpt-web")
    os.system("docker rm chatgpt-web")
    s = f"docker run --name chatgpt-web --rm -itd -p 3002:3002 -e OPENAI_ACCESS_TOKEN={access_token} chenzhaoyu94/chatgpt-web"
    print(s)
    os.system(s)
    print("Restarted!")


# 默认运行时执行一次
job()

# 3天重启一次
schedule.every(3).days.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
