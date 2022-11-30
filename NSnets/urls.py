from django.urls import path
from . import views

urlpatterns = [path('',views.index),
path('About/',views.About),
path('balcony-safety-net/',views.Balcony),
path('BirdPro/',views.BirdProtect),
path('Birdspike/',views.BirdSpikes),
path('cocosafe/',views.ConsafafteyNets),
path('children-safety-net/',views.ChildernSafe),
path('Carparkk/',views.Carpark),
path('coconut-safety-net/',views.Coconut),
path('Cricket/',views.Cricket),
path('duct-area-safety-net/',views.DuctSafe),
path('glass-safety-net/',views.GlassSafe),
path('industrys/',views.industrysafe),
path('/monkey-safety-net/',views.Monkeysafe),
path('pigeon-safety-net/',views.PigeonSafe),
path('PigeonNet/',views.PigeonNet),
path('StairSafe/',views.StaircaseSfatey),
path('SwimSSafe/',views.SwimmingSafe),
#path('sports-net/')



]