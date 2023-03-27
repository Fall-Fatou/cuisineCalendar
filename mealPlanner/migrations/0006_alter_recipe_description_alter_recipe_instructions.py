# Generated by Django 4.1.7 on 2023-03-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealPlanner', '0005_plan_user_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(help_text='Step-by-step instructions for making this recipe.', max_length=1000),
        ),
    ]
