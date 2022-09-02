
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only = True)
    #read only allows to only see reviews during a get request and not add reviews from watchlist in a post request
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id','name','description']
        # exclude = ['active']

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only = True)
    # watchlist = serializers.StringRelatedField(many=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"
    # def get_len_name(self, object):
    #     return len(object.name)
    
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Length of name is too short')
    #     return value
    
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name must not be the same as description')
    #     return data
    

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('The length is too short')
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    #validation is a way of making sure deserialized data is stored in the database properly
    #1. Field-level validation.. def validate_fieldname(self,value)
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Length of name is too short')
    #     return value
    
    #2 OBJECT-LEVEL VALIDATION.. def validate(self,data)
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name must not be the same as description')
    #     return data
    
    #3 Validator, as a function..check top of code