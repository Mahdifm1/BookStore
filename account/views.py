from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .forms import CustomUserCreationForm


class SignUp(View):
    def post(self, request):
        print(request.POST)
        form = CustomUserCreationForm(self.request.POST)
        if form.is_valid():
            print('before save')
            form.save()
            print('after save')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(self.request, user)
            return redirect('main_page')
        else:
            print(form.errors)
            return render(self.request, 'registration/signup.html', {'errors': form.errors, 'form': form})

    def get(self, request):
        form = CustomUserCreationForm(request.POST)
        return render(request, 'registration/signup.html', {'form': form})
