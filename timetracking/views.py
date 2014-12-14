from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect

def sign_in(request):
    pass

def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('timetracking.views.sign_in'))
