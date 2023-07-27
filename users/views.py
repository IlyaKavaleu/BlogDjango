from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user with help UserCreationForm"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def logout(request):
    """in this view we logout users and redirects to home page"""
    if request.method == 'POST':
        logout(request)
        return redirect('learning_logs:index')
