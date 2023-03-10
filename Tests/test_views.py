from django.urls import reverse
from django.test import TestCase

from .models import Plan, Recipe


class TestListPlans(TestCase):

    def test_meal_plan_empty(self):
        response = self.client.get(reverse('plan_list'))
        print(response)
        self.assertQuerysetEqual(response.context['plan_list'], map(repr, []))

    def setUp(self):
        new_recipe = Recipe(name='banana', description='banana', image='', ingredients='banana', instructions='peel')
        new_recipe.save(new_recipe)

        new_plan = Plan(day_of_week='Monday', meal_type='breakfast', recipe=new_recipe)
        new_plan.save(new_plan)

    def test_meal_plan_full(self):
        response = self.client.get(reverse('plan_list'))
        self.assertIsNot(response.context['plan_list'], [])
