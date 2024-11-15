#--------------------# CREATE THE URLS TO BE USED #--------------------#

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SegEstradaViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .perms import AdminOrAnon
from django.shortcuts import redirect
from . import views

#For api/docs using Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API: Monitorização de Tráfego",
        default_version='alpha',
        description="### Descrição das Funcionalidades\n\n"
            "O objetivo é fornecer uma dashboard capaz de analisar e devolver segmentos de estrada, procurados pelo utilizador, de forma rápida e acessível."
            "Além disso, através das permissões criadas, poderá existir mais que um administrador, permitindo a adição e/ou edição de segmentos de estrada e velocidades médias registadas para um determinado local e data.\n"
            "#### Funcionalidades\n\n"
            "- **Lista dos Segmentos de Estrada**: Permite visualizar todos os segmentos de estrada na database - como os dados geográficos, velocidade média e data e hora de registo.\n"
            "- **Detalhes do Segmento de Estrada**: É possível obter os detalhes de um ou mais segmentos de estrada com base nos filtros implementados (através do ID, velocidade e/ou intensidade de tráfego).\n"
            "- **Permissões do Administrador**: Adicionar, editar e remover qualquer segmento de estrada. O administrador também consegue visualizar os segmentos de estrada mais procurados, pelo usuário comum - anónimo.\n"
            "- **Gestão de Utilizadores**: Através de django-admin permite fazer uma gestão dos utilizadores autenticados (e.g. outros administardores).\n",
    ),
    public=True,
    permission_classes=[AdminOrAnon],
)

router = DefaultRouter()
#by doing this, I ensure the router automatically assigns names to these views: list and detail, used in tests.py
router.register(r'segmentos-estrada', SegEstradaViewSet) 

#Redirect to the admin login when clicking the Django Login in Swagger
def custom_login_redirect(request):
    next_url = request.GET.get('next', '')
    return redirect(f'/admin/login/?next={next_url}')


urlpatterns = [
    path('api/models', include(router.urls)),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0)),  #The Swagger docs endpoint
    path('accounts/login/', custom_login_redirect),  #Redirect /accounts/login/ to admin login,
    path('map/', views.map_view, name='map_view'), #Interactive map attempt (still needs work)
]
