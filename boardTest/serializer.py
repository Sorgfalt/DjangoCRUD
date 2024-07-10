import json
from rest_framework import serializers
from .models import BoardTest


class BoardSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    published_date = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create a new board instance and return it as a JSON object.
        """
        board = BoardTest.objects.create(**validated_data)
        return json.dumps({
            "title": board.title,
            "content": board.content,
            "published_date": board.published_date.isoformat()
        })

