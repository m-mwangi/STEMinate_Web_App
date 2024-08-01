from django.db import models
from profiles.models import Profile

class Match(models.Model):
    mentor = models.ForeignKey(Profile, related_name='mentor_matches', on_delete=models.CASCADE)
    mentee = models.ForeignKey(Profile, related_name='mentee_matches', on_delete=models.CASCADE)
    match_score = models.FloatField()

    def __str__(self):
        return f"{self.mentor.user.username} - {self.mentee.user.username}"
