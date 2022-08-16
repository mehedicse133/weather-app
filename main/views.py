from django.shortcuts import render
from .models import City
import requests



api_key= 'You api_key'





def weather(request):
    citys = City.objects.all()
    weather_data = []

    for city in citys:
        wheather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
        
        weather=wheather_data.json()['weather'][0]['main']

        # convert temperture kelvie to celciou
        temp=round(wheather_data.json()['main']['temp'] - 274.15 , 2) 
        image = wheather_data.json()['weather'][0]['icon']
       
        city_weather={
           'city': city,
           'weather': weather,
           'temp': temp,
           'image': image,
        }
        weather_data.append(city_weather)
       
    return render(request,'temp.html',{'city_weather':  weather_data})
