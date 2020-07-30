from django.urls import path
from registration import views
app_name = 'registration'

urlpatterns = [
    path("",views.home , name="home"),
    path("start", views.start, name="start"),
    path("step/one/<str:token>", views.step_one, name="step_one"),
    path("step/two/<str:token>", views.step_two, name="step_two"),
    path("step/three/<str:token>", views.step_three, name="step_three"),
    path("step/four/<str:token>", views.step_four, name="step_four"),
    path("step/five/<str:token>", views.step_five, name="step_five"),
    path("end/<str:token>", views.end, name="end"),
    path("delete", views.delete, name="delete"),
    path("download", views.download, name="download"),
    path("download/<str:token>", views.download_recip, name="download_recip"),
]