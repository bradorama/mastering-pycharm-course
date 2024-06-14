import requests
resp = requests.get('https://weather.talkpython.fm/api/weather?city=irvine&state=CA&country=US&units=imperial')
resp.raise_for_status()
data = resp.json()
temp = data['forecast']['temp']

print(f"Hello World it's {temp} outside!")