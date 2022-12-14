from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """register a new user"""
    if request.method != 'POST':
        """logout entry form"""
        form = UserCreationForm()
    else:
        """process full form"""
        form =UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            """process access and go to home page"""
            login(request, new_user)
            return redirect('learning_logs:index')

    """show entry page"""
    context = {'form': form}
    return render(request, 'registration/register.html', context)