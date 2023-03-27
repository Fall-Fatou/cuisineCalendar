from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Recipe, Plan


# View for the list of recipes
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'mealPlanner/recipe_list.html'
    login_url = 'login'
    redirect_authenticated_user = True

    def get_queryset(self):
        # Get all recipes created by the logged-in user
        return Recipe.objects.filter(user=self.request.user)


# View for a single recipe
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'mealPlanner/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredients = self.object.ingredients.split(',')
        context['ingredients'] = [ingredient.strip() for ingredient in ingredients]
        return context


# View for creating a new recipe
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'mealPlanner/recipe_form.html'
    fields = ['name', 'description', 'ingredients', 'instructions', 'image']
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# View for updating an existing recipe
class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'mealPlanner/recipe_form.html'
    fields = ['name', 'description', 'ingredients', 'instructions', 'image']

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})


# View for deleting an existing recipe
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'mealPlanner/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')


# View for the list of meal plans
class PlanListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = 'mealPlanner/plan_list.html'
    redirect_authenticated_user = True

    # Queryset for the list of meal plans
    '''def get_queryset(self):
        return Plan.objects.all()'''

    # Return only the meal plans created by the current user
    def get_queryset(self):
        return Plan.objects.filter(user=self.request.user)


# View for a single meal plan
class PlanDetailView(DetailView):
    model = Plan
    template_name = 'mealPlanner/plan_detail.html'


# View for creating a new meal plan
class PlanCreateView(LoginRequiredMixin, CreateView):
    model = Plan
    template_name = 'mealPlanner/plan_form.html'
    fields = ['day_of_week', 'meal_type', 'recipe']

    # URL to redirect to on success
    def get_success_url(self):
        return reverse_lazy('plan_list')

    # Method for validating form input

    def form_valid(self, form):  # new
        # Set the user instance of the form to the currently logged-in user
        form.instance.user = self.request.user
        # Call the parent class' form_valid() method with the modified form as argument
        return super().form_valid(form)


# View for updating an existing meal plan
class PlanUpdateView(UpdateView):
    model = Plan
    template_name = 'mealPlanner/plan_form.html'
    # URL to redirect to on success
    fields = ['day_of_week', 'meal_type', 'recipe']

    def get_success_url(self):
        return reverse_lazy('plan_detail', kwargs={'pk': self.object.pk})


# View for deleting an existing meal plan
class PlanDeleteView(DeleteView):
    model = Plan
    template_name = 'mealPlanner/plan_confirm_delete.html'
    success_url = reverse_lazy('plan_list')
