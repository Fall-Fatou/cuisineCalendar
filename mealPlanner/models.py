from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    # Defining fields for Recipe model
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Plan(models.Model):
    # Defining choices for day of week
    DAYS_OF_WEEK = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    )
    # Defining choices for meal type
    MEAL_TYPES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner')
    )
    # Defining fields for Plan model
    day_of_week = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day_of_week} {self.meal_type}"

    def day_of_week_class(self):
        """
        Returns the class name for the day of the week to be used in templates
        """
        class_map = {
            'Monday': 'monday',
            'Tuesday': 'tuesday',
            'Wednesday': 'wednesday',
            'Thursday': 'thursday',
            'Friday': 'friday',
            'Saturday': 'saturday',
            'Sunday': 'sunday'
        }
        return class_map.get(self.day_of_week, '')

