from rest_framework import serializers
from .models import Usuario, PokedexEntry, PokemonUsuario, Tarea, Region

# Serializer para ver las especies (La Pokedex Global)
class PokedexSerializer(serializers.ModelSerializer):
    # Traemos el nombre de la región en vez de solo el ID, es mas estetico para el frontend
    region_nombre = serializers.CharField(source='region.nombre', read_only=True)
    
    class Meta:
        model = PokedexEntry
        fields = ['id', 'numero', 'nombre', 'tipo_principal', 'region_nombre', 'sprite_url']

# Serializer para TUS Pokemon (PC y Equipo)
class MiPokemonSerializer(serializers.ModelSerializer):
    especie_info = PokedexSerializer(source='especie', read_only=True)

    class Meta:
        model = PokemonUsuario
        fields = ['id', 'apodo', 'nivel', 'experiencia', 'en_equipo', 'especie', 'especie_info']
        read_only_fields = ['nivel', 'experiencia', 'entrenador'] 

    def validate_en_equipo(self, value):
        # Si el usuario está intentando poner este pokemon en su equipo
        if value:
            request = self.context.get('request')
            # Contamos cuántos pokemon ya tiene en el equipo
            equipo_actual = PokemonUsuario.objects.filter(entrenador=request.user, en_equipo=True).count()
            
            # Si estamos editando un pokemon que YA estaba en el equipo, lo permitimos
            if self.instance and self.instance.en_equipo:
                return value
                
            # Si ya tiene 6, bloqueamos la acción
            if equipo_actual >= 6:
                raise serializers.ValidationError("¡Tu equipo ya está lleno! No puedes tener más de 6 Pokémon activos.")
        return value
    
# Serializer de Tareas (Pomodoro)
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        read_only_fields = ['usuario', 'fecha_creacion']

# Serializer de Usuario (Perfil)
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'foto_perfil', 'tema_app', 'pomo_tiempo_trabajo', 'pomo_tiempo_descanso']

# Register para JWT (Registro de Usuario), no viene por default por ende lo creamos
class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('username', 'password', 'email', 'foto_perfil')

    def create(self, validated_data):
        # Es CRÍTICO usar create_user para que la contraseña se encripte
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            foto_perfil=validated_data.get('foto_perfil', None)
        )
        return user