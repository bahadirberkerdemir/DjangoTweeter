from django.urls import path
from . import views
app_name = 'TwitApp'

urlpatterns = [
    path('', views.listtweet, name='listtweet'), #domain.com/TwitApp/
    path('addtweet/', views.addtweet, name='addtweet'), #domain.com/TwitApp/addtweet/
    path('tweetbyform', views.addTweetbyForm, name='addtweetbyform'),
    path('tweetbymodelform', views.addtweetbymodelform, name='addtweetbymodelform'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('deletetweet/<int:id>', views.deletetweet, name='deletetweet')
]