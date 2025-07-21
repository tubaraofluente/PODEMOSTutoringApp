from django.views import View
from django.shortcuts import render
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class MentoresView(View):
    def get(self, request, *args, **kwargs):
        mentores = Mentor.objects.all()
        return render(request, 'mentores.html', {'mentores': mentores})

class SessoesView(View):
    def get(self, request, *args, **kwargs):
        sessoes = SessaoMentoria.objects.filter(mentorado__usuario=request.user)
        return render(request, 'sessoes.html', {'sessoes': sessoes})