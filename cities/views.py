from django.shortcuts import render

from cities.models import (
    City,
    Landmark,
    Hotel,
    Restaurant,
    Event,
    Park,
    Review,
    Museum,
    Country,
    TouristAttraction,
)


def city_list_view(request):
    city_list = City.objects.all()
    return render(request, 'cities/city_list.html', {'city_list': city_list})


def landmark_list_view(request):
    landmark_list = Landmark.objects.all()
    return render(request, 'cities/landmark_list.html', {'landmark_list': landmark_list})


def hotel_list_view(request):
    hotel_list = Hotel.objects.all()
    return render(request, 'cities/hotel_list.html', {'hotel_list': hotel_list})


def restaurant_list_view(request):
    restaurant_list = Restaurant.objects.all()
    return render(request, 'cities/restaurant_list.html', {'restaurant_list': restaurant_list})


def event_list_view(request):
    event_list = Event.objects.all()
    return render(request, 'cities/event_list.html', {'event_list': event_list})


def park_list_view(request):
    park_list = Park.objects.all()
    return render(request, 'cities/park_list.html', {'park_list': park_list})


def review_list_view(request):
    review_list = Review.objects.all()
    return render(request, 'cities/review_list.html', {'review_list': review_list})


def museum_list_view(request):
    museum_list = Museum.objects.all()
    return render(request, 'cities/museum_list.html', {'museum_list': museum_list})


def country_list_view(request):
    country_list = Country.objects.all()
    return render(request, 'cities/country_list.html', {'country_list': country_list})


def tourist_attraction_list_view(request):
    tourist_attraction_list = TouristAttraction.objects.all()
    return render(request, 'cities/touristattraction_list.html', {'tourist_attraction_list': tourist_attraction_list})


