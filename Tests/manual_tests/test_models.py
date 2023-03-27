from django.contrib.auth.models import User
from mealPlanner.models import Recipe, Plan
from django.test import TestCase


class RecipeModelTest(TestCase):

    def test_recipe_model(self):
        """
        Test that the Recipe model can be created and saved correctly.
        """
        # Create a test user
        user = User.objects.create(username='testuser', password='testpass')
        # Create a new recipe object
        recipe = Recipe(name='Banana', description='A delicious banana', image='',
                        ingredients='1 Banana',
                        instructions='Peel the Banana',
                        user=user)

        # Save the recipe object to the database
        recipe.save()

        # Retrieve the recipe from the database
        saved_recipe = Recipe.objects.get(name='Banana')

        # Assert that the recipe was saved correctly
        self.assertEqual(saved_recipe.name, 'Banana')
        self.assertEqual(saved_recipe.description, 'A delicious banana')
        self.assertEqual(saved_recipe.image, '')
        self.assertEqual(saved_recipe.ingredients, '1 Banana')
        self.assertEqual(saved_recipe.instructions, 'Peel the Banana')


class PlanModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.recipe = Recipe.objects.create(
            name='Banana', description='A delicious banana', image='',
            ingredients='1 Banana',
            instructions='Peel the Banana',
            user=self.user
        )
        self.plan = Plan.objects.create(
            day_of_week='Monday',
            meal_type='breakfast',
            recipe=self.recipe,
            user=self.user
        )

    def test_plan_day_of_week(self):
        self.assertEqual(self.plan.day_of_week, 'Monday')

    def test_plan_meal_type(self):
        self.assertEqual(self.plan.meal_type, 'breakfast')

    def test_plan_recipe(self):
        self.assertEqual(self.plan.recipe, self.recipe)

    def test_plan_user(self):
        self.assertEqual(self.plan.user, self.user)

    def test_day_of_week_class(self):
        self.assertEqual(self.plan.day_of_week_class(), 'monday')
