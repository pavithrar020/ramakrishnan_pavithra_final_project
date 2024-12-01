# forms.py

from django import forms
from .models import City, Landmark, Hotel, Restaurant, Event, Review, Museum, Country


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country', 'population', 'description']


class LandmarkForm(forms.ModelForm):
    class Meta:
        model = Landmark
        fields = ['city', 'name', 'description', 'landmark_type']


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['city', 'name', 'address', 'rating']


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['city', 'name', 'cuisine', 'rating']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['city', 'name', 'date', 'description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['city', 'comment', 'rating']


class MuseumForm(forms.ModelForm):
    class Meta:
        model = Museum
        fields = ['city', 'name']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'population', 'capital']