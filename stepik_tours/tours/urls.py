from django.urls import path
from tours.views import MainView, DepartureView, TourView


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path(
        'departure/<str:departure>',
        DepartureView.as_view(),
        name='departure',
    ),
    path('tour/<int:id>/', TourView.as_view(), name='tour')
]
