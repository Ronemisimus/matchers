from django.shortcuts import render
from django.views import generic
# Create your views here.

class LoginView(generic.View):
    template_name = 'user_app/login.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
