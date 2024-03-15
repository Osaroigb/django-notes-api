from .models import Note
from rest_framework import serializers

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
    

    def validate_title(self, value):
        # Ensure title is not blank
        if not value.strip():
            raise serializers.ValidationError("The title must not be blank.")
        
        return value


    def validate(self, data):
        # Ensure the content has a minimum length of 10 characters
        if len(data.get('content', '')) < 10:
            raise serializers.ValidationError("The content must be at least 10 characters long.")
        
        return data