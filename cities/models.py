from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    population = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - Population: {self.population}, Country: {self.country}"

    class Meta:
        verbose_name_plural = "cities"
        ordering = ['name']


class Landmark(models.Model):
    HUMAN_MADE = 'Human-made'
    NATURAL = 'Natural'
    LANDMARK_TYPES = [
        (HUMAN_MADE, 'Human-made'),
        (NATURAL, 'Natural'),
    ]

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    landmark_type = models.CharField(
        max_length=50,
        choices=LANDMARK_TYPES,
        default=HUMAN_MADE,
    )

    def __str__(self):
        return f"{self.name} ({self.get_landmark_type_display()}) - {self.city.name}"

    class Meta:
        ordering = ['name']


class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name} - Rating: {self.rating}"

    class Meta:
        ordering = ['name']


class Restaurant(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name} - Cuisine: {self.cuisine}, Rating: {self.rating}"

    class Meta:
        ordering = ['name']


class Event(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - Date: {self.date}"

    class Meta:
        ordering = ['name']


class Park(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    area = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - Area: {self.area}"

    class Meta:
        ordering = ['name']


class Review(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"Review-{self.id}: {self.comment[:30]}... - Rating: {self.rating}"

    class Meta:
        ordering = ['id']


class Museum(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    capital = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - Population: {self.population}, Capital: {self.capital}"

    class Meta:
        verbose_name_plural = "countries"


class TouristAttraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.city.name}"

    class Meta:
        ordering = ['name']


