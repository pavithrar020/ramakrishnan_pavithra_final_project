# Generated by Django 4.1 on 2023-08-07 04:22
from django.db import migrations

LANDMARKS = [
    {
        'name': 'Tokyo Tower',
        'city_name': 'Tokyo',
        'description': 'Tokyo Tower is a famous landmark and communications tower in Tokyo, Japan.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'The Bund',
        'city_name': 'Shanghai',
        'description': 'The Bund is a waterfront area in Shanghai, China, known for its historic buildings and modern skyline.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'São Paulo Cathedral',
        'city_name': 'São Paulo',
        'description': 'São Paulo Cathedral is a major religious landmark in São Paulo, Brazil, known for its stunning architecture and cultural significance.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Gateway of India',
        'city_name': 'Mumbai',
        'description': 'The Gateway of India is an iconic monument in Mumbai, India, representing the city\'s colonial history and architectural beauty.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Forbidden City',
        'city_name': 'Beijing',
        'description': 'The Forbidden City is an ancient imperial palace in Beijing, China, renowned for its grandeur and historical significance.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Great Sphinx of Giza',
        'city_name': 'Cairo',
        'description': 'The Great Sphinx of Giza is a monumental statue with the head of a human and the body of a lion, located near the Giza Pyramids in Cairo, Egypt.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Lalbagh Fort',
        'city_name': 'Dhaka',
        'description': 'Lalbagh Fort is a 17th-century Mughal fort in Dhaka, Bangladesh, known for its architectural beauty and historical significance.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Osaka Castle',
        'city_name': 'Osaka',
        'description': 'Osaka Castle is a historic Japanese castle in Osaka, Japan, famous for its imposing appearance and cultural heritage.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Mohatta Palace',
        'city_name': 'Karachi',
        'description': 'Mohatta Palace is an elegant 20th-century palace in Karachi, Pakistan, now serving as a museum and art gallery.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Hagia Sophia',
        'city_name': 'Istanbul',
        'description': 'Hagia Sophia is a former Byzantine church and Ottoman mosque in Istanbul, Turkey, now a museum and an architectural marvel.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Badshahi Mosque',
        'city_name': 'Lahore',
        'description': 'Badshahi Mosque is a magnificent Mughal-era mosque in Lahore, Pakistan, known for its impressive architecture and historical importance.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Grand Palace',
        'city_name': 'Bangkok',
        'description': 'The Grand Palace is a majestic royal palace complex in Bangkok, Thailand, representing the grandeur of Thai architecture and royalty.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Saint Basil\'s Cathedral',
        'city_name': 'Moscow',
        'description': 'Saint Basil\'s Cathedral is a vibrant and colorful Orthodox church located in Moscow, Russia, an iconic symbol of the country.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Charminar',
        'city_name': 'Hyderabad',
        'description': 'Charminar is a historical monument and mosque in Hyderabad, India, famous for its unique architecture and cultural significance.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Gyeongbokgung Palace',
        'city_name': 'Seoul',
        'description': 'Gyeongbokgung Palace is a grand royal palace in Seoul, South Korea, representing the Joseon Dynasty\'s architectural brilliance.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Kinshasa Arts Academy',
        'city_name': 'Kinshasa',
        'description': 'Kinshasa Arts Academy is a prominent cultural institution in Kinshasa, Democratic Republic of the Congo, promoting arts and creativity.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'National Monument',
        'city_name': 'Jakarta',
        'description': 'The National Monument is a towering monument in Jakarta, Indonesia, symbolizing the country\'s struggle for independence.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Huaca Pucllana',
        'city_name': 'Lima',
        'description': 'Huaca Pucllana is an ancient adobe and clay pyramid in Lima, Peru, representing the archaeological significance of the region.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Tower Bridge',
        'city_name': 'London',
        'description': 'Tower Bridge is a famous Victorian-era drawbridge in London, United Kingdom, a symbol of the city\'s engineering and architectural prowess.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Saigon Central Post Office',
        'city_name': 'Ho Chi Minh City',
        'description': 'Saigon Central Post Office is a historic post office building in Ho Chi Minh City, Vietnam, known for its colonial-era architecture.',
        'landmark_type': 'Human-made',
    },
    {
        'name': 'Gold Museum',
        'city_name': 'Bogotá',
        'description': 'Gold Museum is a renowned museum in Bogotá, Colombia, exhibiting an extensive collection of pre-Columbian gold artifacts.',
        'landmark_type': 'Human-made',
    },
]


def add_landmark_data(apps, schema_editor):
    Landmark = apps.get_model('cities', 'Landmark')
    City = apps.get_model('cities', 'City')

    for landmark_data in LANDMARKS:
        city_name = landmark_data.pop('city_name')
        city = City.objects.get(name=city_name)

        landmark_data['city'] = city
        Landmark.objects.create(**landmark_data)


def remove_landmark_data(apps, schema_editor):
    Landmark = apps.get_model('cities', 'Landmark')
    for landmark_data in LANDMARKS:
        try:
            landmark = Landmark.objects.get(name=landmark_data['name'], city__name=landmark_data['city_name'])
            landmark.delete()
        except Landmark.DoesNotExist:
            # Handle the case when the landmark does not exist in the database
            pass


class Migration(migrations.Migration):
    dependencies = [
        ('cities', '0011_load_citytest_data'),
    ]

    operations = [
        migrations.RunPython(
            add_landmark_data,
            remove_landmark_data
        )
    ]
