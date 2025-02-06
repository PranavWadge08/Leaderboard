from django import forms
from challenge.models import ChallengeSubmission, Challenge

class ChallengeSubmissionForm(forms.ModelForm):
    flag = forms.CharField(max_length=800)

    class Meta:
        model = ChallengeSubmission
        fields = ('challenge', 'flag')

    def clean(self):
        cleaned_data = super().clean()
        challenge = cleaned_data.get("challenge")
        flag = cleaned_data.get("flag")
        if challenge and flag:
            valid_challenge = Challenge.objects.filter(
                id=challenge.id, flag=flag).exists()
            if not valid_challenge:
                self.add_error(None, "Invalid Flag.")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
