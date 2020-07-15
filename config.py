import os

if os.environ.get('API_KEY'):
    API_KEY = os.environ.get('API_KEY')
    API_TOKEN = os.environ.get('API_TOKEN')
    ACCESS_KEY = os.environ.get('ACCESS_KEY')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
else:
    from twitter_config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

    API_KEY = API_KEY
    API_SECRET = API_SECRET
    ACCESS_TOKEN = ACCESS_TOKEN
    ACCESS_SECRET = ACCESS_SECRET
