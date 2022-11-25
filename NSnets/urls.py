from django.urls import path
from . import views

urlpatterns = [path('',views.index),
path('About/',views.About),
path('Balcony/',views.Balcony),
path('BirdPro/',views.BirdProtect),
path('Birdspike/',views.BirdSpikes),
path('cocosafe/',views.ConsafafteyNets),
path('Child/',views.ChildernSafe),
path('Carparkk/',views.Carpark),
path('Coconut/',views.Coconut),
path('Cricket/',views.Cricket),
path('Duct/',views.DuctSafe),
path('GlassSafee/',views.GlassSafe),
path('industrys/',views.industrysafe),
path('Monkey/',views.Monkeysafe),
path('PigeonS/',views.PigeonSafe),
path('PigeonNet/',views.PigeonNet),
path('StairSafe/',views.StaircaseSfatey),
path('SwimSSafe/',views.SwimmingSafe),



]