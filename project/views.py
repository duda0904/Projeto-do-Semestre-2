from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tutorials.models import AplicacaoTutorial

@login_required
def homepage(request):
    apl = AplicacaoTutorial.objects.all()
    return render(request, 'project/index.html', {'aplicacao':apl})

@login_required
def adminpage(request):
    if request.user.is_staff:
        return render(request, 'project/admin.html')
    else:
        return HttpResponse('Você não tem permissão de Admin')