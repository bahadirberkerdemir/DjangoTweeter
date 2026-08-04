from django.contrib import admin
from TwitApp.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin) :
    fieldsets=[
        ('Msg Group', {"fields" : ["message"]}),
        ('Nick Group', {"fields" : ["nickname"]}) #groups fields, better for multiple fields
    ]

    #fields = ['message', 'nickname' ] # can change places of bars

admin.site.register(Tweet,TweetAdmin)
