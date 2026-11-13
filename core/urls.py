from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'funcionarios', views.FuncionarioViewSet, basename='funcionario')
router.register(r'lista-funcionarios', views.ListafuncionarioViewSet, basename='lista-funcionario')
router.register(r'nova-solitacao', views.CriarSolicitacaoViewSet, basename='nova-solitacao')
router.register(r'gerente-funcionario', views.FuncionaGerenteViewSet, basename='gerente-funcionario')
router.register(r'receber-solitacao', views.ReceberSolicitacaoViewSet, basename='receber-solitacao')
router.register(r'lista-solitacao', views.ListaViewSet, basename='lista-solitacao')

urlpatterns = [
    path('', include(router.urls)),
]
