import requests, json, re, os, random

GUILD_ID = os.getenv('GUILD_ID')
ROLE_ID = os.getenv('ROLE_ID')
HCPING_ID = os.getenv('HCPING_ID')
BOT_TOKEN = os.getenv('ADMIN_BOT_TOKEN')

'''
Get word of the day
'''
resp = requests.get("https://www.merriam-webster.com/word-of-the-day")
wotd = re.search(">(.*)(?=<\/h2)", resp.text)[1]

print(f"Word of the day: {wotd}")

response = requests.patch(f"https://discord.com/api/v9/guilds/{GUILD_ID}/roles/{ROLE_ID}",
    headers = {
        'Authorization': f"Bot {BOT_TOKEN}",
        'Content-Type': 'application/json'
    }, data = json.dumps({ "name": wotd }))

if response.status_code != 200:
    print(f"Status code: {response.status_code}\nBody: {response.text}")
    raise "Non 200 status code"

requests.get(f"https://hc-ping.com/{HCPING_ID}") # Health check
