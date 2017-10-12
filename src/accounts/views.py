from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import DetailView
from django.views import View
from .models import UserProfile

# Create your views here.
User = get_user_model()

class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name='accounts/user_detail.html'

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context['following'] = UserProfile.objects.is_following(self.request.user, self.get_object())
        return context

class UserFollowView(View):
    def get(self, request, username, *args, **kwarg):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", username=username)
        # url = reverse("profiles:detail", kwargs={"username": username})
        # HttpResponseRedirect(url)S
        