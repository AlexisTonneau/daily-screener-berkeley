import requests
import os


def reboot_heroku():
    r = requests.delete(f"https://api.heroku.com/apps/{os.getenv('APP_ID')}/dynos/{os.getenv('DYNO_NAME')}",
                        headers={'Authorization': f"Bearer {os.getenv('API_KEY')}",
                                 'Accept': 'application/vnd.heroku+json; version=3'})
    print(r.text)
