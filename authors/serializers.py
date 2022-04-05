from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import Author

#
# class AuthorsModelSerializers(HyperlinkedModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'




class AuthorsModelSerializers(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ('uid',)
