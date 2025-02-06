import time
from django.db import models
from django.db.models import Sum, Count, Max

from accounts.models import User
from .utils import update_leaderboard


class Challenge(models.Model):
    """Stores the CTF Challenge details"""
    name = models.CharField(
        max_length=255, help_text='Name of the challenge')
    points = models.IntegerField()
    flag = models.CharField(max_length=800, unique=True)

    class Meta:
        db_table = "challenge"
    
    def __str__(self) -> str:
        return self.name


class ChallengeSubmission(models.Model):
    """Stores correct flag submissions from contestants."""
    contestant = models.ForeignKey(User, on_delete=models.PROTECT)
    challenge = models.ForeignKey(Challenge, on_delete=models.PROTECT)
    time = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = "challenge_submissions"

    def __str__(self) -> str:
        return ''.join([self.contestant.first_name, ':', self.challenge.name])

    def save(self, *args, **kwargs):
        self.time = time.time()
        super(ChallengeSubmission, self).save(*args, **kwargs)
        update_leaderboard(
            ChallengeSubmission.objects
            .values('contestant', 'contestant__first_name', 'contestant__last_name')
            .annotate(
                points=Sum('challenge__points'),
                flags=Count('id'),
                last=Max('time')
            )
            .order_by('-points', 'last'), {"id": self.contestant.id, "name": self.contestant.first_name})
