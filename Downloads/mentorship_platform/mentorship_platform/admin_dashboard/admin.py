from django.contrib import admin
from user_management.models import User
from profiles.models import Profile
from matching.models import Match
from communication.models import Message
from resources.models import Resource
from community.models import Forum, Topic

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Match)
admin.site.register(Message)
admin.site.register(Resource)
admin.site.register(Forum)
admin.site.register(Topic)
