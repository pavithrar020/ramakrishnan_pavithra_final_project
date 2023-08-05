from django.urls import path

from cities.views import (
    city_list_view,
    landmark_list_view,
    hotel_list_view,
    restaurant_list_view,
    event_list_view,
    park_list_view,
    review_list_view,
    museum_list_view,
    country_list_view,
    tourist_attraction_list_view,
)

urlpatterns = [
    path('city/', city_list_view),
    path('landmark/', landmark_list_view),
    path('hotel/', hotel_list_view),
    path('restaurant/', restaurant_list_view),
    path('event/', event_list_view),
    path('park/', park_list_view),
    path('review/', review_list_view),
    path('museum/', museum_list_view),
    path('country/', country_list_view),
    path('touristattraction/', tourist_attraction_list_view),
]
