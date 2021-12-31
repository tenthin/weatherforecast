from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_API_KEY'
    city = 'Las Vegas'
    
    return render(request,'weather/weather.html')