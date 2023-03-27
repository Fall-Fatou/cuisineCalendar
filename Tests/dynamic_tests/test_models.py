from django.test import TestCase
from mealPlanner.models import Plan, Recipe
from django.contrib.auth.models import User


class TestRecipeModel(TestCase):
    def setUp(self):
        # Creating a user for the tests
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Creating a recipe object to be used for the tests
        self.recipe = Recipe.objects.create(
            name='Banana',
            description='A delicious banana',
            image='',
            ingredients='1 Banana',
            instructions='Peel the banana',
            user=self.user
        )

    def test_recipe_name_label(self):
        # Testing if the verbose name of the 'name' field of Recipe is 'name'
        field_label = self.recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_recipe_description_label(self):
        # Testing if the verbose name of the 'description' field is 'description'
        field_label = self.recipe._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_recipe_model_str(self):
        # Testing if the __str__ method of Recipe returns the expected string
        self.assertEqual(str(self.recipe), 'Banana')

    def test_recipe_name_max_length(self):
        # Testing if the max length of the 'name' field of Recipe is 200
        max_length = self.recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_recipe_description_max_length(self):
        # Testing if the max length of the 'description' field of Recipe is 500
        max_length = self.recipe._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)

    def test_recipe_instructions_max_length(self):
        # Testing if the max length of the 'instructions' field of Recipe is 1000
        max_length = self.recipe._meta.get_field('instructions').max_length
        self.assertEqual(max_length, 1000)

    def test_recipe_instructions_help_text(self):
        """Testing if the help text of the 'instructions' field of Recipe is 'Step-by-step instructions for making
                 this recipe."""
        help_text = self.recipe._meta.get_field('instructions').help_text
        self.assertEqual(help_text, 'Step-by-step instructions for making this recipe.')


class TestPlanModel(TestCase):
    def setUp(self):
        # Creating a user for the tests
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Creating a recipe
        self.recipe = Recipe.objects.create(
            name="salade au thon",
            description="easy",
            image="",
            ingredients="salade, 1 thon",
            instructions="mélanger le tout",
            user=self.user
        )

        # Creating a plan object with the recipe
        self.plan = Plan.objects.create(
            day_of_week="Monday",
            meal_type="Dinner",
            recipe=self.recipe,
            user=self.user
        )

    def test_plan_model_str(self):
        # Testing if the __str__ method of Plan returns the expected string
        self.assertEqual(str(self.plan), "Monday Dinner - salade au thon")

    def test_plan_day_of_week_label(self):
        # Testing if the verbose name of the 'day_of_week' field of Plan is 'day of week'
        field_label = self.plan._meta.get_field('day_of_week').verbose_name
        self.assertEqual(field_label, 'day of week')

    def test_plan_meal_type_label(self):
        # Testing if the verbose name of the 'meal_type' field of Plan is 'meal type'
        field_label = self.plan._meta.get_field('meal_type').verbose_name
        self.assertEqual(field_label, 'meal type')

    def test_plan_recipe_label(self):
        # Testing if the verbose name of the 'recipe' field of Plan is 'recipe'
        field_label = self.plan._meta.get_field('recipe').verbose_name
        self.assertEqual(field_label, 'recipe')

    def test_plan_user_label(self):
        # Testing if the verbose name of the 'user' field of Plan is 'user'
        field_label = self.plan._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_plan_day_of_week_max_length(self):
        # Testing if the max length of the 'day_of_week' field of Plan is 20
        max_length = self.plan._meta.get_field('day_of_week').max_length
        self.assertEqual(max_length, 20)

    def test_plan_day_of_week_choices(self):
        # Testing if the choices of the 'day_of_week' field of Plan are "DAYS_OF_WEEK"
        choices = self.plan._meta.get_field('day_of_week').choices
        self.assertEqual(choices, (('Monday', 'Monday'),
                                   ('Tuesday', 'Tuesday'),
                                   ('Wednesday', 'Wednesday'),
                                   ('Thursday', 'Thursday'),
                                   ('Friday', 'Friday'),
                                   ('Saturday', 'Saturday'),
                                   ('Sunday', 'Sunday')))

    def test_plan_meal_type_max_length(self):
        # Testing if the max length of the 'meal_type' field of Plan is 20
        max_length = self.plan._meta.get_field('meal_type').max_length
        self.assertEqual(max_length, 20)

    def test_plan_meal_type_choices(self):
        # Testing if the choices of the 'meal_type' field of Plan are "MEAL_TYPES"
        choices = self.plan._meta.get_field('meal_type').choices
        self.assertEqual(choices, (('Breakfast', 'breakfast'), ('Lunch', 'lunch'), ('Dinner', 'dinner')))

    def test_recipe_is_foreign_key(self):
        # Testing if the 'recipe' field of Plan is Foreignkey
        self.assertIsInstance(self.recipe, Recipe)

    def test_user_is_foreign_key(self):
        # Testing if the 'user' field of Plan is Foreignkey
        self.assertIsInstance(self.user, User)


