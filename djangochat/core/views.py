from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm
"""
    The function "frontpage" returns a rendered HTML template called "frontpage.html" when a request is
    made.
    
    :param request: The request parameter is an object that represents the HTTP request made by the
    user. It contains information such as the user's browser, IP address, and any data sent with the
    request
    :return: the rendered template 'core/frontpage.html'.
"""
def frontpage(request):
    return render(request, 'core/frontpage.html')

"""
    The `signup` function handles the signup process, including form validation, saving the user, and
    logging them in.
    
    :param request: The request object represents the HTTP request that the user made to access the
    view. It contains information about the user's request, such as the HTTP method (GET, POST, etc.),
    the user's session, and any data submitted in the request
    :return: a rendered HTML template called 'signup.html' with the form as a context variable.
"""

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})