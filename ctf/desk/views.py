from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.forms import BaseModelForm
from django.views.generic import TemplateView, CreateView
from django.db.models import Count, Sum, Exists, OuterRef, Q
from django.urls import reverse_lazy
from challenge.models import Challenge, ChallengeSubmission
from .forms import ChallengeSubmissionForm


class HomeView(LoginRequiredMixin, TemplateView):
    """Renders Home view for logged in users."""
    template_name = "desk/home.html"


class ScoreView(LoginRequiredMixin, TemplateView):
    """Renders CTF Score for logged in users."""
    template_name = "desk/score.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["challenges"] = Challenge.objects.annotate(
            is_done=Exists(ChallengeSubmission.objects.filter(
                contestant=self.request.user, challenge=OuterRef('pk'))))
        context['totals'] = context['challenges'].aggregate(
            score=Sum('points', filter=Q(is_done=True)),
            done=Count('id', filter=Q(is_done=True)),
            points=Sum('points'), challenges=Count('id'))
        return context


class FlagSubmitView(LoginRequiredMixin, CreateView):
    """Renders Flag Submission view for logged in users."""
    form_class = ChallengeSubmissionForm
    template_name = "desk/flag_submit.html"
    success_url = reverse_lazy("desk:submit_flag")

    def get_initial(self):
        initial = super().get_initial()
        if self.request.GET.get('challenge'):
            initial['challenge'] = self.request.GET.get('challenge')
        return initial

    def form_valid(self, form: BaseModelForm):
        form.instance.contestant = self.request.user
        if ChallengeSubmission.objects.filter(
            contestant=self.request.user, challenge=form.instance.challenge).first():
            form.add_error(None, "Already submitted flag for this challenge.")
            return self.form_invalid(form)
        messages.success(self.request, 'Yay! That was a correct flag.')
        return super().form_valid(form)


class LeaderBoardView(TemplateView):
    template_name = "desk/leaderboard.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['totals'] = Challenge.objects.values(
            'id').annotate(challenges=Count('id'), points=Sum('points'))
        return context
    
