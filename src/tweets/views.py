from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    DeleteView,
    DetailView, 
    ListView, 
    UpdateView
)

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet

# CRUD - function and class based views 
# Create=======================================================================
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'
    # login_url = '/admin/'

# Retrieve=======================================================================
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

class TweetListView(ListView):
    queryset = Tweet.objects.all()
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context

# Update===============================================================================
# combination of detail and create
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = "/tweet/"
    # login_url = 

# Delete==============================================================================
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("home")
    template_name = 'tweets/delete_confirm.html'

# List / Search=======================================================================
