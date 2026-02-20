from rest_framework import serializers
from .models import Usuario, PokedexEntry, PokemonUsuario, Tarea, Region

# Serializer para ver las especies (La Pokedex Global)
class PokedexSerializer(serializers.ModelSerializer):
    region_nombre = serializers.CharField(source='region.nombre', read_only=True)
    
    class Meta:
        model = PokedexEntry
        # AÑADIDO: 'sprite_shiny_url' para que el frontend pueda previsualizarlo
        fields = [
            'id', 'numero', 'nombre', 'tipo_principal', 
            'tipo_secundario', 'region_nombre', 'sprite_url', 'sprite_shiny_url'
        ]

# Serializer para TUS Pokemon (PC y Equipo)
class MiPokemonSerializer(serializers.ModelSerializer):
    especie_info = PokedexSerializer(source='especie', read_only=True)

    class Meta:
        model = PokemonUsuario
        # AÑADIDO: 'es_shiny' para saber qué sprite mostrar en el Dashboard/PC
        fields = ['id', 'apodo', 'nivel', 'experiencia', 'en_equipo', 'es_shiny', 'especie', 'especie_info']
        read_only_fields = ['nivel', 'experiencia', 'entrenador'] 

    def validate_en_equipo(self, value):
        if value:
            request = self.context.get('request')
            equipo_actual = PokemonUsuario.objects.filter(entrenador=request.user, en_equipo=True).count()
            
            if self.instance and self.instance.en_equipo:
                return value
                
            if equipo_actual >= 6:
                raise serializers.ValidationError("¡Tu equipo ya está lleno! No puedes tener más de 6 Pokémon activos.")
        return value

# Los demás serializers se mantienen igual
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        read_only_fields = ['usuario', 'fecha_creacion']

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'foto_perfil', 'tema_app', 'pomo_tiempo_trabajo', 'pomo_tiempo_descanso', 'password']
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        
        # Actualizar otros campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Si se proporciona una contraseña, establecerla correctamente
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('username', 'password', 'email', 'foto_perfil')

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            foto_perfil=validated_data.get('foto_perfil', None)
        )
        return user