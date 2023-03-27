from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from mealPlanner.models import Plan, Recipe


class RecipeViewTests(TestCase):

    def setUp(self):
        # Create a test client
        self.client = Client()
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Log the user in to the client
        self.client.login(username='testuser', password='testpass')

        # Create a test recipe
        self.recipe = Recipe.objects.create(
            name='Banana',
            description='A delicious banana',
            image='',
            ingredients='1 Banana',
            instructions='Peel the banana',
            user=self.user
        )

    def test_recipe_list_view(self):
        # Test the Recipe List view
        response = self.client.get(reverse('recipe_list'))
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains the recipe name
        self.assertContains(response, 'Banana')
        # Assert that the response contains description
        self.assertContains(response, 'A delicious banana')

    def test_recipe_detail_view(self):
        # Test the Recipe Detail view
        response = self.client.get(reverse('recipe_detail', kwargs={'pk': self.recipe.pk}))
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains the recipe name
        self.assertContains(response, 'Banana')
        # Assert that the response contains description
        self.assertContains(response, 'A delicious banana')
        # Assert that the response contains the ingredients
        self.assertContains(response, '1 Banana')
        # Assert that the response contains the instructions
        self.assertContains(response, 'Peel the banana')
        # Assert that the response doesn't contain any image
        self.assertNotContains(response, 'static/image/background_image.png')

    def test_recipe_create_view(self):
        # Test the Recipe Create view
        response = self.client.post(reverse('recipe_create'), {
            'name': 'Salade au thon',
            'description': 'easy',
            'ingredients': 'salade, thon, sel',
            'instructions': 'mélanger tout',
        })
        # Assert that the response status code is 302 Found (redirect)
        self.assertEqual(response.status_code, 302)
        # Assert that the response redirects to the Recipe List view
        self.assertRedirects(response, reverse('recipe_list'))
        # Assert that the new Recipe object was created in the database
        self.assertTrue(Recipe.objects.filter(name='Salade au thon',
                                              description='easy',
                                              ingredients='salade, thon, sel',
                                              instructions='mélanger tout', ).exists())

    def test_recipe_update_view(self):
        # Test the Recipe Update view
        response = self.client.post(reverse('recipe_update', kwargs={'pk': self.recipe.pk}), {
            'name': 'Salade au thon',
            'description': 'easy to prepare',
            'ingredients': 'salade, thon, salt, vinegar, peper',
            'instructions': 'mix all',
        })
        # Assert that the response status code is 302 Found (redirect)
        self.assertEqual(response.status_code, 302)
        # Assert that the response redirects to the Plan Detail view for the updated Plan object
        self.assertRedirects(response, reverse('recipe_detail', kwargs={'pk': self.recipe.pk}))
        # Assert that the description of the Recipe object was updated in the database
        self.assertEqual(Recipe.objects.get(pk=self.recipe.pk).description, 'easy to prepare')
        # Assert that the ingredients of the Recipe object was updated in the database
        self.assertEqual(Recipe.objects.get(pk=self.recipe.pk).ingredients, 'salade, thon, salt, vinegar, peper')
        # Assert that the instructions of the Recipe object is no more "mélanger tout"
        self.assertNotEqual(Recipe.objects.get(pk=self.recipe.pk).instructions, 'mélanger tout')

    def test_recipe_delete_view(self):
        # Send a POST request to delete view with the recipe's primary key in the URL kwargs
        response = self.client.post(reverse('recipe_delete', kwargs={'pk': self.recipe.pk}))
        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # Check that the response redirects to the recipe list page
        self.assertRedirects(response, reverse('recipe_list'))
        # Check that the recipe with the primary key used in the test has been deleted
        self.assertFalse(Recipe.objects.filter(pk=self.recipe.pk).exists())


class PlanViewTests(TestCase):

    def setUp(self):
        # Create a test client
        self.client = Client()
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Log the user in to the client
        self.client.login(username='testuser', password='testpass')

        # Create a test recipe
        self.recipe = Recipe.objects.create(
            name='Banana',
            description='A delicious banana',
            image='',
            ingredients='1 Banana',
            instructions='Peel the banana',
            user=self.user
        )

        # Create a test plan
        self.plan = Plan.objects.create(
            day_of_week='Monday',
            meal_type='Breakfast',
            recipe=self.recipe,
            user=self.user
        )

    def test_plan_list_view(self):
        # Test the Plan List view
        response = self.client.get(reverse('plan_list'))
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains the day of the week
        self.assertContains(response, 'Monday')
        # Assert that the response contains the meal type
        self.assertContains(response, 'Breakfast')
        # Assert that the response contains the recipe name
        self.assertContains(response, 'Banana')

    def test_plan_detail_view(self):
        # Test the Plan Detail view
        response = self.client.get(reverse('plan_detail', kwargs={'pk': self.plan.pk}))
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains the day of the week
        self.assertContains(response, 'Monday')
        # Assert that the response contains the meal type
        self.assertContains(response, 'Breakfast')
        # Assert that the response contains the recipe name
        self.assertContains(response, 'Banana')

    def test_plan_create_view(self):
        # Test the Plan Create view
        response = self.client.post(reverse('plan_create'), {
            'day_of_week': 'Tuesday',
            'meal_type': 'Lunch',
            'recipe': self.recipe.id,
        })
        # Assert that the response status code is 302 Found (redirect)
        self.assertEqual(response.status_code, 302)
        # Assert that the response redirects to the Plan List view
        self.assertRedirects(response, reverse('plan_list'))
        # Assert that the new Plan object was created in the database
        self.assertTrue(Plan.objects.filter(day_of_week='Tuesday', meal_type='Lunch', recipe=self.recipe).exists())

    def test_plan_update_view(self):
        # Test the Plan Update view
        response = self.client.post(reverse('plan_update', kwargs={'pk': self.plan.pk}), {
            'day_of_week': 'Monday',
            'meal_type': 'Dinner',
            'recipe': self.recipe.id,
        })
        # Assert that the response status code is 302 Found (redirect)
        self.assertEqual(response.status_code, 302)
        # Assert that the response redirects to the Plan Detail view for the updated Plan object
        self.assertRedirects(response, reverse('plan_detail', kwargs={'pk': self.plan.pk}))
        # Assert that the meal type of the Plan object was updated in the database
        self.assertEqual(Plan.objects.get(pk=self.plan.pk).meal_type, 'Dinner')

    def test_plan_delete_view(self):
        # Send a POST request to delete view with the plan's primary key in the URL kwargs
        response = self.client.post(reverse('plan_delete', kwargs={'pk': self.plan.pk}))
        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # Check that the response redirects to the plan list page
        self.assertRedirects(response, reverse('plan_list'))
        # Check that the plan with the primary key used in the test has been deleted
        self.assertFalse(Plan.objects.filter(pk=self.plan.pk).exists())
