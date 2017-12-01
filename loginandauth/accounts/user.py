from django.shortcuts import HttpResponseRedirect, render
from forms import LoginUserForm
from django.contrib import auth

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'GET' and request.GET.has_key('next'):
       next_page = request.GET['next']
    else:
        next_page = '/'
    if next_page == "/accounts/logout":
        next_page = '/'
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(request.POST['next'])

    else:
        form = LoginUserForm(request)
    kwargs = {
        'request':request,
        'form':form,
        'next':next_page,
    }
    return render(request, 'accounts/login.html', kwargs)