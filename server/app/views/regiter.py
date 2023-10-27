from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class UserRegistrationView(CreateView):
    template_name = 'registration_form.html'  # Specify the template for the registration form
    form_class = UserCreationForm  # Use the built-in UserCreationForm provided by Django
    success_url = reverse_lazy('login')  # Redirect to the login page upon successful user registration

    def form_valid(self, form):
        # Log the user in upon successful registration
        login(self.request, form.save())
        return super().form_valid(form)
