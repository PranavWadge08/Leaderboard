from django.contrib import admin
from .models import Challenge, ChallengeSubmission


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'points', 'flag')

admin.site.register(Challenge, ChallengeAdmin)


class ChallengeSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'contestant', 'challenge', 'time')

admin.site.register(ChallengeSubmission, ChallengeSubmissionAdmin)

