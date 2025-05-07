from django.urls import path

from . import views
app_name = "polls"
urlpatterns = [
    path('',views.index, name = "index"),
    path('register/', views.register, name = "register"),
    path('login/', views.loginuser, name = "login"),
    path('logout/', views.logout, name = "logout"),
    path('<int:question_id>/', views.detail, name = "detail"),
    path('<int:question_id>/results/', views.results, name = "results"),
    path('<int:question_id>/vote/', views.vote, name = "vote"),
    path('pollquestion/', views.pollquestion, name="pollquestion")
]
