


import requests
from django.shortcuts import render
from django.conf import settings

def weather_view(request):
    city = request.GET.get('city', 'karachi') # the city is set to karachi by defult we can 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=ef079e46c6e94505499bb1ae44ef4034&units=metric" # this is the url or the query from which we comunicate with the api and fetch data
    response = requests.get(url)
    data = response.json()

    context = {
        'city': city, # the city is js a local variable so we dont fetch it from the api we print the one we got in the input
        'weather': data.get('weather', [{}])[0].get('description', 'Incorrect City'), # we exract the weather from the api results and pass it in the html
        'temperature': data.get('main', {}).get('temp', '∞'), # and we aslo axract the temp from the api and send it to the html,   
    }

    return render(request, 'weather/weather.html', context)
