from rest_framework import serializers
from posts.models import Post

# Defines field getting serialized/ Deserialized 
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model=Post
        fields=['id','title','content','author']



    # Create and return a new post instance given validated data
    def create(self,validated_data):
        return Post.objects.create(**validated_data)

    #Updates and return an existing post instance given validate data
    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.content=validated_data.get('content',instance.content)
        instance.author=validated_data.get('author',instance.author)
        instance.save()

        return instance
         
