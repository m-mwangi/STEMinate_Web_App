# matching/views.py
from django.shortcuts import render
from profiles.models import Profile
from .models import Match

def match_profiles(request):
    # Dummy matching logic for demonstration
    profiles = Profile.objects.all()
    for mentor in profiles.filter(user__is_staff=True):
        for mentee in profiles.filter(user__is_staff=False):
            score = calculate_match_score(mentor, mentee)
            Match.objects.create(mentor=mentor, mentee=mentee, match_score=score)
    return render(request, 'matching/matches.html', {'matches': Match.objects.all()})

def calculate_match_score(mentor, mentee):
    # Replace with actual matching logic
    return 0.5
