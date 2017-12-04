from django.shortcuts import HttpResponseRedirect, render
from forms import LoginUserForm, EditUserForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from accounts.permission import permission_verify
from django.contrib.auth import get_user_model

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






@login_required()
@permission_verify()
def user_list(request):
    temp_name = "accounts/accounts-header.html"
    all_user = get_user_model().objects.all()
    kwargs = {
        'temp_name': temp_name,
        'all_user': all_user,
    }
    return render(request, 'accounts/user_list.html', kwargs)


def user_add(request):
    return render(request, '<h1>user add page</h1>')

def user_del(request):
    return render(request, '<h1>user del page</h1>')

@login_required
@permission_verify()
def user_edit(request, ids):
    user = get_user_model().objects.get(id=ids)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            status = 1
        else:
            status = 2
    else:
        form = EditUserForm(instance=user)
    return render(request, 'accounts/user_edit.html', locals())








def reset_password(request):
    return render(request, '<h1>reset password page')
