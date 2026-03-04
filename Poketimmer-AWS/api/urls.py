from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import TareaViewSet, MiPokemonViewSet, PokedexViewSet, UsuarioViewSet, RegistroView, finalizar_entrenamiento

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')
router.register(r'mis-pokemon', MiPokemonViewSet, basename='mipokemon')
router.register(r'pokedex', PokedexViewSet, basename='pokedex')
router.register(r'perfil', UsuarioViewSet, basename='perfil')

urlpatterns = [
    # Rutas del Router (CRUDs)
    path('', include(router.urls)),

    # Rutas de Autenticación
    path('auth/registro/', RegistroView.as_view(), name='registro'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Ruta para finalizar el entrenamiento de un Pokémon
    path('entrenamiento/', finalizar_entrenamiento, name='finalizar_entrenamiento'),
]