from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.permission import permission_verify

# Create your views here.

@login_required()
@permission_verify()
def index(request):
    return render(request, "navi/index.html", locals())