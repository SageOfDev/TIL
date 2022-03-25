from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
        # id = serializers.IntegerField(read_only=True)
        # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
        # code = serializers.CharField(style={'base_template': 'textarea.html'})
        # linenos = serializers.BooleanField(required=False)
        # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
        # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Snippet' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    # 역관계는 이부분을 언급해주어야한다고 하는데, 왠지 자동으로 되는 것 같다. 나중에 다시 확인해보자
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
