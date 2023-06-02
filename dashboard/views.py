from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required # login_required means that only authorized users can access to this method
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')