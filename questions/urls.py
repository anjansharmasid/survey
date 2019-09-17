from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('test/<int:testIdentifier_id>/<int:candidate_id>/<int:question_id>/', views.test),
    path('questions', views.questions),
    path('answers',  views.answers),
    path('candidate',  views.candidate),
    path('candidateanswers', views.candidateanswers),
    path('testresult', views.testresult),
    path('starttest', views.starttest),
    path('retake/<str:username>/<int:candidate_id>/', views.retake),
    path('test_first/<int:candidate_id>/<int:testIdentifier_id>/', views.test_first),
    path('redirect/<int:candidate_id>/', views.redirect),
    path('home', views.home)

]

