from rest_framework import serializers


from . import models


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ('id', 'title', 'body', 'created', 'modified')
        read_ony = ('created', 'modified')
