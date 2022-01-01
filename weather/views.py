import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_API_KEY'
    city = 'Las Vegas'
    
    r = requests.get(url.format(city))
    print(r.text)

    return render(request,'weather/weather.html')