from django.urls import path
from .views import HomePageView,TrialPageView,BusMarkerPage
from .import views
urlpatterns = [
    path('',HomePageView.as_view(),name='landingindex'),
    path('locc',views.incidence,name='incidence'),
    path('trial',TrialPageView.as_view(),name='trial'),
    path('get-markers',views.get_markers,name='get_markers'),
    path('bus-markers/<yatayat>',views.bus_markers,name='bus_markers'),
    path('bus',BusMarkerPage.as_view(),name='bus-page'),


]