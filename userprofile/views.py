from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import UserProfile


def signup(request):
    # making logic of sign up process
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # if everything is valid - we save the user
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)

            return redirect('/log-in/')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })