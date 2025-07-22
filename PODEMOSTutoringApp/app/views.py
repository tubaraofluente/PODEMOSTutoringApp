# C:\Users\felip\PODEMOSTutoringApp\app\views.py

from django.views.generic import TemplateView

# View para a página inicial
class IndexView(TemplateView):
    template_name = "app/index.html" # Você precisará criar este arquivo HTML depois

# View para a página de mentores
class MentoresView(TemplateView):
    template_name = "app/mentores.html" # Você precisará criar este arquivo HTML depois

# View para a página de sessões
class SessoesView(TemplateView):
    template_name = "app/sessoes.html" # Você precisará criar este arquivo HTML depois

# View para a página de áreas de conhecimento
class AreasConhecimentoView(TemplateView):
    template_name = "app/areas_conhecimento.html" # Você precisará criar este arquivo HTML depois

# View para a página de agendamento de sessão
class AgendarSessaoView(TemplateView):
    template_name = "app/agendar_sessao.html" # Você precisará criar este arquivo HTML depois