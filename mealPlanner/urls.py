from django.urls import path
from . import views

urlpatterns = [
    # URL for the home page
    path('', views.index, name='index'),


    # URL for recipes
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/new/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),


    # URL for plans
    path('plans/', views.PlanListView.as_view(), name='plan_list'),
    path('plans/<int:pk>/', views.PlanDetailView.as_view(), name='plan_detail'),
    path('plans/new/', views.PlanCreateView.as_view(), name='plan_create'),
    path('plans/<int:pk>/edit/', views.PlanUpdateView.as_view(), name='plan_update'),
    path('plans/<int:pk>/delete/', views.PlanDeleteView.as_view(), name='plan_delete'),
]
