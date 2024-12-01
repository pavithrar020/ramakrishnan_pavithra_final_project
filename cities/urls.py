from django.urls import path

from cities import views
from cities.views import (
    CityList,
    LandmarkList,
    HotelList,
    RestaurantList,
    EventList,
    ReviewList,
    MuseumList,
    CountryList,
    CityDetail,
    LandmarkDetail,
    HotelDetail,
    RestaurantDetail,
    EventDetail,
    ReviewDetail,
    MuseumDetail,
    CountryDetail,
)


urlpatterns = [

    path('city/',
         CityList.as_view(),
         name='cities_city_list_urlpattern'),

    path('city/<int:city_id>/',
         CityDetail.as_view(),
         name='city-detail'),

    path('city/<int:city_id>/update/',
         views.update_city,
         name='update-city'),

    path('city/<int:city_id>/delete/',
         views.delete_city,
         name='delete-city'),

    path('city/create/',
         views.create_city,
         name='create-city'),

    path('landmark/',
         LandmarkList.as_view(),
         name='cities_landmark_list_urlpattern'),

    path('landmark/<int:landmark_id>/',
         LandmarkDetail.as_view(),
         name='landmark-detail'),

    path('landmark/<int:landmark_id>/update/',
         views.update_landmark,
         name='update-landmark'),

    path('landmark/<int:landmark_id>/delete/',
         views.delete_landmark,
         name='delete-landmark'),

    path('landmark/create/',
         views.create_landmark,
         name='create-landmark'),

    path('hotel/',
         HotelList.as_view(),
         name='cities_hotel_list_urlpattern'),

    path('hotel/<int:hotel_id>/',
         HotelDetail.as_view(),
         name='hotel-detail'),

    path('hotel/<int:hotel_id>/update/',
         views.update_hotel,
         name='update-hotel'),

    path('hotel/<int:hotel_id>/delete/',
         views.delete_hotel,
         name='delete-hotel'),

    path('hotel/create/',
         views.create_hotel,
         name='create-hotel'),

    path('restaurant/',
         RestaurantList.as_view(),
         name='cities_restaurant_list_urlpattern'),

    path('restaurant/<int:restaurant_id>/',
         RestaurantDetail.as_view(),
         name='restaurant-detail'),

    path('restaurant/<int:restaurant_id>/update/',
         views.update_restaurant,
         name='update-restaurant'),

    path('restaurant/<int:restaurant_id>/delete/',
         views.delete_restaurant,
         name='delete-restaurant'),

    path('restaurant/create/',
         views.create_restaurant,
         name='create-restaurant'),

    path('event/',
         EventList.as_view(),
         name='cities_event_list_urlpattern'),

    path('event/<int:event_id>/',
         EventDetail.as_view(),
         name='event-detail'),

    path('event/<int:event_id>/update/',
         views.update_event,
         name='update-event'),

    path('event/<int:event_id>/delete/',
         views.delete_event,
         name='delete-event'),

    path('event/create/',
         views.create_event,
         name='create-event'),

    path('review/',
         ReviewList.as_view(),
         name='cities_review_list_urlpattern'),

    path('review/<int:review_id>/',
         ReviewDetail.as_view(),
         name='review-detail'),

    path('review/<int:review_id>/update/',
         views.update_review,
         name='update-review'),

    path('review/<int:review_id>/delete/',
         views.delete_review,
         name='delete-review'),

    path('review/create/',
         views.create_review,
         name='create-review'),

    path('museum/',
         MuseumList.as_view(),
         name='cities_museum_list_urlpattern'),

    path('museum/<int:museum_id>/',
         MuseumDetail.as_view(),
         name='museum-detail'),

    path('museum/<int:museum_id>/update/',
         views.update_museum,
         name='update-museum'),

    path('museum/<int:museum_id>/delete/',
         views.delete_museum,
         name='delete-museum'),

    path('museum/create/',
         views.create_museum,
         name='create-museum'),

    path('country/',
         CountryList.as_view(),
         name='cities_country_list_urlpattern'),

    path('country/<int:country_id>/',
         CountryDetail.as_view(),
         name='country-detail'),

    path('country/<int:country_id>/update/',
         views.update_country,
         name='update-country'),

    path('country/<int:country_id>/delete/',
         views.delete_country,
         name='delete-country'),

    path('country/create/',
         views.create_country,
         name='create-country'),
]
