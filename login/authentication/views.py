from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.views.decorators.cache import cache_control
from django.contrib import messages

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signin(request):
    if 'username' in request.session:
        return redirect(index) 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            request.session['username'] = username
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')  

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if 'username' in request.session:
        return render(request, 'index.html')
    return redirect('signin')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    if 'username' in request.session:
        request.session.flush() 
    return redirect('signin')