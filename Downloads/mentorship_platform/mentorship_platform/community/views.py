from django.shortcuts import render
from .models import Forum, Topic

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'community/forum_list.html', {'forums': forums})

def topic_list(request, forum_id):
    topics = Topic.objects.filter(forum_id=forum_id)
    return render(request, 'community/topic_list.html', {'topics': topics})
