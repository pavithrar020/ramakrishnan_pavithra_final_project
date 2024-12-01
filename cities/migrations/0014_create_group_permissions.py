from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    city_permissions = permission_class.objects.filter(content_type__app_label='cities',
                                                       content_type__model='city')

    country_permissions = permission_class.objects.filter(content_type__app_label='cities',
                                                          content_type__model='country')

    event_permissions = permission_class.objects.filter(content_type__app_label='cities',
                                                        content_type__model='event')

    hotel_permissions = permission_class.objects.filter(content_type__app_label='cities',
                                                        content_type__model='hotel')

    landmark_permissions = permission_class.objects.filter(content_type__app_label='cities',
                                                           content_type__model='landmark')

    museum_permissions = permission_class.objects.filter(content_type__app_label='cities',
                                                         content_type__model='permission')

    restaurant_permissions = permission_class.objects.filter(content_type__app_label='cities',
                                                             content_type__model='restaurant')

    review_permissions = permission_class.objects.filter(content_type__app_label='cities',
                                                         content_type__model='review')

    perm_view_city = permission_class.objects.filter(content_type__app_label='cities',
                                                     content_type__model='city',
                                                     codename='view_city')

    perm_view_country = permission_class.objects.filter(content_type__app_label='cities',
                                                        content_type__model='country',
                                                        codename='view_country')

    perm_view_event = permission_class.objects.filter(content_type__app_label='cities',
                                                      content_type__model='event',
                                                      codename='view_event')

    perm_view_hotel = permission_class.objects.filter(content_type__app_label='cities',
                                                      content_type__model='hotel',
                                                      codename='view_hotel')

    perm_view_landmark = permission_class.objects.filter(content_type__app_label='cities',
                                                         content_type__model='landmark',
                                                         codename='view_landmark')

    perm_view_museum = permission_class.objects.filter(content_type__app_label='cities',
                                                       content_type__model='museum',
                                                       codename='view_museum')

    perm_view_restaurant = permission_class.objects.filter(content_type__app_label='cities',
                                                           content_type__model='restaurant',
                                                           codename='view_restaurant')

    perm_view_review = permission_class.objects.filter(content_type__app_label='cities',
                                                       content_type__model='review',
                                                       codename='view_review')

    ci_user_permissions = chain(perm_view_city,
                                perm_view_country,
                                perm_view_event,
                                perm_view_hotel,
                                perm_view_landmark,
                                perm_view_museum,
                                perm_view_restaurant,
                                perm_view_review,
                                )

    ci_touristguide_permissions = chain(perm_view_city,
                                        city_permissions,
                                        event_permissions,
                                        hotel_permissions,
                                        restaurant_permissions,
                                        perm_view_country,
                                        landmark_permissions,
                                        country_permissions,
                                        museum_permissions
                                        )

    ci_tourist_permissions = chain(perm_view_country,
                                   perm_view_landmark,
                                   perm_view_hotel,
                                   perm_view_museum,
                                   perm_view_restaurant,
                                   city_permissions,
                                   event_permissions,
                                   review_permissions
                                   )

    my_groups_initialization_list = [
        {
            "name": "ci_user",
            "permissions_list": ci_user_permissions,
        },
        {
            "name": "ci_touristguide",
            "permissions_list": ci_touristguide_permissions,
        },
        {
            "name": "ci_tourist",
            "permissions_list": ci_tourist_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('cities', '0013_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
