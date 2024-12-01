from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import ListView

from cities.forms import CityForm, LandmarkForm, HotelForm, RestaurantForm, EventForm, ReviewForm, MuseumForm, \
    CountryForm

from cities.models import (
    City,
    Landmark,
    Hotel,
    Restaurant,
    Event,
    Review,
    Museum,
    Country,
)
from cities.utils import PageLinksMixin


class CityList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 12
    model = City
    permission_required = 'cities.view_city'


class CityDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'cities.view_city'
    permission_required = 'cities.delete_city'
    permission_required = 'cities.add_city'
    permission_required = 'cities.change_city'

    def get(self, request, city_id):
        city = get_object_or_404(City, pk=city_id)
        return render(request, 'cities/city_detail.html', {'city': city})


def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)

    if request.method == 'POST':
        city.delete()
        return redirect('cities_city_list_urlpattern')  # Use the correct name for the city list URL pattern

    return render(request, 'cities/city_confirm_delete.html', {'city': city})


def create_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities_city_list_urlpattern')
    else:
        form = CityForm()

    return render(request, 'cities/city_create.html', {'form': form})


def update_city(request, city_id):
    city = get_object_or_404(City, id=city_id)

    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('city-detail', city_id=city_id)  # Use the correct URL name here for city detail view
    else:
        form = CityForm(instance=city)

    return render(request, 'cities/city_form.html', {'form': form, 'city': city})


class LandmarkList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 12
    model = Landmark
    permission_required = 'cities.view_landmark'


class LandmarkDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'cities.view_landmark'
    permission_required = 'cities.add_landmark'
    permission_required = 'cities.change_landmark'
    permission_required = 'cities.delete_landmark'

    def get(self, request, landmark_id):
        landmark = get_object_or_404(Landmark, pk=landmark_id)
        return render(request, 'cities/landmark_detail.html', {'landmark': landmark})


def update_landmark(request, landmark_id):
    landmark = get_object_or_404(Landmark, id=landmark_id)

    if request.method == 'POST':
        form = LandmarkForm(request.POST, instance=landmark)
        if form.is_valid():
            form.save()
            return redirect('landmark-detail', landmark_id)  # Redirect to landmark detail view after successful update
    else:
        form = LandmarkForm(instance=landmark)

    return render(request, 'cities/landmark_form.html', {'form': form, 'landmark': landmark})


def delete_landmark(request, landmark_id):
    landmark = get_object_or_404(Landmark, id=landmark_id)

    if request.method == 'POST':
        landmark.delete()
        return redirect('cities_landmark_list_urlpattern')  # Redirect to landmark list view after successful deletion

    return render(request, 'cities/landmark_confirm_delete.html', {'landmark': landmark})


def create_landmark(request):
    if request.method == 'POST':
        form = LandmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities_landmark_list_urlpattern')
    else:
        form = LandmarkForm()

    return render(request, 'cities/landmark_create.html', {'form': form})


class HotelList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Hotel
    permission_required = 'cities.view_hotel'
    permission_required = 'cities.add_hotel'
    permission_required = 'cities.change_hotel'
    permission_required = 'cities.delete_hotel'


def update_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel-detail', hotel_id)
    else:
        form = HotelForm(instance=hotel)

    return render(request, 'cities/hotel_form.html', {'form': form, 'hotel': hotel})


def delete_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        hotel.delete()
        return redirect('cities_hotel_list_urlpattern')

    return render(request, 'cities/hotel_confirm_delete.html', {'hotel': hotel})


def create_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities_hotel_list_urlpattern')
    else:
        form = HotelForm()

    return render(request, 'cities/hotel_create.html', {'form': form})


class HotelDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'cities.view_hotel'

    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        return render(request, 'cities/hotel_detail.html', {'hotel': hotel})


class RestaurantList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Restaurant
    permission_required = 'cities.view_restaurant'


class RestaurantDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'cities.view_restaurant'
    permission_required = 'cities.add_restaurant'
    permission_required = 'cities.change_restaurant'
    permission_required = 'cities.delete_restaurant'

    def get(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        return render(request, 'cities/restaurant_detail.html', {'restaurant': restaurant})


def update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant-detail', restaurant_id)
    else:
        form = RestaurantForm(instance=restaurant)

    return render(request, 'cities/restaurant_form.html', {'form': form, 'restaurant': restaurant})


def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        restaurant.delete()
        return redirect('cities_restaurant_list_urlpattern')

    return render(request, 'cities/restaurant_confirm_delete.html', {'restaurant': restaurant})


def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities_restaurant_list_urlpattern')
    else:
        form = RestaurantForm()

    return render(request, 'cities/restaurant_create.html', {'form': form})


class EventList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Event
    permission_required = 'cities.view_event'


class EventDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'cities.view_event'
    permission_required = 'cities.add_event'
    permission_required = 'cities.change_event'
    permission_required = 'cities.delete_event'

    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        return render(request, 'cities/event_detail.html', {'event': event})


def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-detail', event_id)
    else:
        form = EventForm(instance=event)

    return render(request, 'cities/event_form.html', {'form': form, 'event': event})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        event.delete()
        return redirect('cities_event_list_urlpattern')

    return render(request, 'cities/event_confirm_delete.html', {'event': event})


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities_event_list_urlpattern')
    else:
        form = EventForm()

    return render(request, 'cities/event_create.html', {'form': form})


class ReviewList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Review
    permission_required = 'cities.view_review'


class ReviewDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'cities.view_review'
    permission_required = 'cities.add_review'
    permission_required = 'cities.change_review'
    permission_required = 'cities.delete_review'

    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        return render(request, 'cities/review_detail.html', {'review': review})


def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review-detail', review_id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'cities/review_form.html', {'form': form, 'review': review})


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('cities_restaurant_list_urlpattern')

    return render(request, 'cities/review_confirm_delete.html', {'review': review})


def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities_review_list_urlpattern')
    else:
        form = ReviewForm()

    return render(request, 'cities/review_create.html', {'form': form})


class MuseumList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Museum
    permission_required = 'cities.view_museum'


class MuseumDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'cities.view_museum'
    permission_required = 'cities.add_museum'
    permission_required = 'cities.change_museum'
    permission_required = 'cities.delete_museum'

    def get(self, request, museum_id):
        museum = get_object_or_404(Museum, pk=museum_id)
        return render(request, 'cities/museum_detail.html', {'museum': museum})


def update_museum(request, museum_id):
    museum = get_object_or_404(Museum, id=museum_id)

    if request.method == 'POST':
        form = MuseumForm(request.POST, instance=museum)
        if form.is_valid():
            form.save()
            return redirect('museum-detail', museum_id)
    else:
        form = MuseumForm(instance=museum)

    return render(request, 'cities/museum_form.html', {'form': form, 'museum': museum})


def delete_museum(request, museum_id):
    museum = get_object_or_404(Museum, id=museum_id)

    if request.method == 'POST':
        museum.delete()
        return redirect('cities_museum_list_urlpattern')

    return render(request, 'cities/museum_confirm_delete.html', {'museum': museum})


def create_museum(request):
    if request.method == 'POST':
        form = MuseumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities_museum_list_urlpattern')
    else:
        form = MuseumForm()

    return render(request, 'cities/museum_create.html', {'form': form})


class CountryList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Country
    permission_required = 'cities.view_country'


class CountryDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'cities.view_country'
    permission_required = 'cities.add_country'
    permission_required = 'cities.change_country'
    permission_required = 'cities.delete_country'

    def get(self, request, country_id):
        country = get_object_or_404(Country, pk=country_id)
        return render(request, 'cities/country_detail.html', {'country': country})


def update_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)

    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country-detail', country_id)
    else:
        form = CountryForm(instance=country)

    return render(request, 'cities/country_form.html', {'form': form, 'country': country})


def delete_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)

    if request.method == 'POST':
        country.delete()
        return redirect('cities_country_list_urlpattern')

    return render(request, 'cities/country_confirm_delete.html', {'country': country})


def create_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities_country_list_urlpattern')
    else:
        form = CountryForm()

    return render(request, 'cities/country_create.html', {'form': form})
