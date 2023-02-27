# Generated by Django 4.1.7 on 2023-02-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealPlanner', '0003_ingredient_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='salade'),
            preserve_default=False,
        ),
    ]
