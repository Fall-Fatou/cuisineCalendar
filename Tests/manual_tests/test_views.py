from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from mealPlanner.models import Recipe, Plan


class TestRecipeListView(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        # Create some recipes
        self.recipe1 = Recipe.objects.create(
            name='Banana', description='A delicious banana', image='',
            ingredients='1 Banana',
            instructions='Peel the Banana',
            user=self.user
        )
        self.recipe2 = Recipe.objects.create(
            name="salade au thon",
            description="easy",
            image="",
            ingredients="salade, 1 thon",
            instructions="mélanger le tout",
            user=self.user
        )

    def test_recipe_list_view_empty(self):
        # Log in as a user
        self.client.login(username='testuser', password='testpass')

        # Delete all recipes
        Recipe.objects.all().delete()

        # Get the recipe list view
        response = self.client.get(reverse('recipe_list'))

        # Check that the response contains the appropriate message
        self.assertContains(response, "No recipe has been created at this time.")

    def test_recipe_list_view_with_recipes(self):
        # Log in as a user
        self.client.login(username='testuser', password='testpass')

        # Get the recipe list view
        response = self.client.get(reverse('recipe_list'))

        # Check that the response contains the names of both recipes
        self.assertContains(response, self.recipe1.name)
        self.assertContains(response, self.recipe2.name)

    def test_recipe_detail_view(self):
        # Log in as a user
        self.client.login(username='testuser', password='testpass')

        # Get the recipe detail view for recipe1
        response = self.client.get(reverse('recipe_detail', args=[self.recipe1.id]))

        # Check that the response contains the name, description, ingredients, and instructions of recipe1
        self.assertContains(response, self.recipe1.name)
        self.assertContains(response, self.recipe1.description)
        self.assertContains(response, self.recipe1.ingredients)
        self.assertContains(response, self.recipe1.instructions)
        # Including negative test for user
        self.assertNotContains(response, self.recipe1.user)


class PlanListViewTest(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some recipes
        self.recipe1 = Recipe.objects.create(
            name='Banana', description='A delicious banana', image='',
            ingredients='1 Banana',
            instructions='Peel the Banana',
            user=self.user
        )
        self.recipe2 = Recipe.objects.create(
            name="salade au thon",
            description="easy",
            image="",
            ingredients="salade, 1 thon",
            instructions="mélanger le tout",
            user=self.user
        )

        # Create 2 meal plans for the user
        self.plan1 = Plan.objects.create(
            day_of_week="Monday",
            meal_type="Dinner",
            recipe=self.recipe1,
            user=self.user
        )

        self.plan2 = Plan.objects.create(
            day_of_week="Thursday",
            meal_type="Lunch",
            recipe=self.recipe2,
            user=self.user
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('plan_list'))
        self.assertRedirects(response, '/accounts/login/?next=/mealPlanner/plans/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/mealPlanner/plans/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('plan_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('plan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealPlanner/plan_list.html')

    def test_lists_all_plans(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('plan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Monday')
        self.assertContains(response, 'Thursday')

    def test_list_only_user_plans(self):
        # Create another user
        test_user2 = User.objects.create_user(username='testuser2', password='testpass2')
        test_user2.save()

        self.recipe = Recipe.objects.create(
            name="salade au thon",
            description="easy",
            image="",
            ingredients="salade, 1 thon",
            instructions="mélanger le tout",
            user=self.user
        )

        # Create a meal plan for test_user2
        Plan.objects.create(
            user=test_user2,
            day_of_week="Saturday",
            meal_type="Breakfast",
            recipe=self.recipe
        )

        # Log in as test_user1 and check that only their meal plans are listed
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('plan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Monday')
        self.assertContains(response, 'Thursday')
        self.assertNotContains(response, 'Saturday')
