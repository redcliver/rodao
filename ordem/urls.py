from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ordem),
    url(r'^busca', views.busca),
    url(r'^abrir', views.abrir),
    url(r'^editar', views.editar),
    url(r'^imprimir/$', views.GeneratePdf.as_view()),
    url(r'^pre_imprimir', views.pre_imprimir),
    url(r'^cancellar', views.cancellar),
    url(r'^cancelar', views.cancelar),
    url(r'^excluir', views.excluir),
    url(r'^ver', views.ver),
    url(r'^add_serv', views.add_serv),
    url(r'^add_prod', views.add_prod),
    url(r'^total_ordem', views.total_ordem),
    url(r'^total_mes', views.total_mes),
    url(r'^fechar', views.fechar),
    ]
