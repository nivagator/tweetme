from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet

# Create your views here.

# CRUD - function and class based views 

# Create=======================================================================
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'
    # login_url = '/admin/'

   
#funciton based create view-------------------------
# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#     context = {
#         "form":form
#     }
#     return render(request, 'tweets/creat_view.html', context)

#--- end function based create view


# Retrieve=======================================================================
class TweetDetailView(DetailView):
    # template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     return obj

class TweetListView(ListView):
    # template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)
        return context

# -----starting with FUNCION BASED VIEWS-----------------------
# def tweet_detail_view(request, pk=None): # pk == id
#     # obj = Tweet.objects.get(pk=pk) # GET from database
#     obj = get_object_or_404(Tweet, pk=pk)
#     print(obj)
#     context = {
#         "object": obj,
#     } 
#     return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/detail_list.html", context)
# ------END FUNCTION BASED VIEWS ---------------------------------

# Update=======================================================================
# combination of detail and create
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = "/tweet/"
    # login_url = 

# Delete=======================================================================

# List / Search=======================================================================
