from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Recipe, Plan


# View for the home page
def index(request):
    return render(request, 'mealPlanner/index.html')


# View for the list of recipes
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'mealPlanner/recipe_list.html'

    def get_queryset(self):
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

    # Queryset for the list of meal plans
    '''def get_queryset(self):
        return Plan.objects.all()'''

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
    '''def form_valid(self, form):
        response = super().form_valid(form)
        self.object.save()
        return response'''

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# View for updating an existing meal plan
class PlanUpdateView(UpdateView):
    model = Plan
    template_name = 'mealPlanner/plan_form.html'
    fields = ['day_of_week', 'meal_type', 'recipe']  # URL to redirect to on success

    def get_success_url(self):
        return reverse_lazy('plan_detail', kwargs={'pk': self.object.pk})


# View for deleting an existing meal plan
class PlanDeleteView(DeleteView):
    model = Plan
    template_name = 'mealPlanner/plan_confirm_delete.html'
    success_url = reverse_lazy('plan_list')
