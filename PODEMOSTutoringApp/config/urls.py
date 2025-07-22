from django.contrib import admin
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('mentores/', MentoresView.as_view(), name='mentores'),
    path('sessoes/', SessoesView.as_view(), name='sessoes'),
    path('areas/', AreasConhecimentoView.as_view(), name='areas'),
    path('agendar/', AgendarSessaoView.as_view(), name='agendar'),
    path('conta/', include('django.contrib.auth.urls')),
]