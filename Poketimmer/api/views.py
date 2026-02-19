from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Usuario, PokedexEntry, PokemonUsuario, Tarea
from .serializers import UsuarioSerializer, PokedexSerializer, MiPokemonSerializer, TareaSerializer, RegistroSerializer


# --- TAREAS ---
class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        tarea_antigua = self.get_object()
        tarea_nueva = serializer.save()

        if not tarea_antigua.completada and tarea_nueva.completada:
            equipo = PokemonUsuario.objects.filter(entrenador=self.request.user, en_equipo=True)
            for pokemon in equipo:
                pokemon.ganar_experiencia(25) 
                
    # Acción de borrar mediante POST (coincide con frontend: tareas/borrar/)
    @action(detail=False, methods=['post'], url_path='borrar')
    def borrar_por_post(self, request):
        item_id = request.data.get('id')
        if item_id:
            tarea = Tarea.objects.filter(id=item_id, usuario=request.user).first()
            if tarea:
                tarea.delete()
                return Response({'status': 'eliminado correctamente'}, status=status.HTTP_200_OK)
            return Response({'error': 'No encontrada o no tienes permisos'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'ID no proporcionado en el POST'}, status=status.HTTP_400_BAD_REQUEST)


# --- POKÉMON Y POKÉDEX ---
class MiPokemonViewSet(viewsets.ModelViewSet):
    serializer_class = MiPokemonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PokemonUsuario.objects.filter(entrenador=self.request.user)

    def perform_create(self, serializer):
        serializer.save(entrenador=self.request.user)

class PokedexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PokedexEntry.objects.all()
    serializer_class = PokedexSerializer
    permission_classes = [permissions.IsAuthenticated]


# --- USUARIOS Y REGISTRO ---
class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Usuario.objects.filter(id=self.request.user.id)
    
class RegistroView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistroSerializer


# --- ENTRENAMIENTO POMODORO ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def finalizar_entrenamiento(request):
    equipo = PokemonUsuario.objects.filter(entrenador=request.user, en_equipo=True)
    exp_ganada = 50 
    
    for pokemon in equipo:
        pokemon.ganar_experiencia(exp_ganada)
        
    return Response({
        "mensaje": f"¡Entrenamiento completado! Tu equipo ha ganado {exp_ganada} EXP."
    }, status=status.HTTP_200_OK)