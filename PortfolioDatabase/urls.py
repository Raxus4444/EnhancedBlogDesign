from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('hobbies/<int:hobby_id>', views.hobby_detail, name="hobby_details"),
    path('portfolio/<int:portfolio_id>', views.portfolio_detail, name="portfolio_details"),
]
