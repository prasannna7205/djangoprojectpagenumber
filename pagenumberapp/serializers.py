from rest_framework.serializers import ModelSerializer
from pagenumberapp.models import Addpagelist
class AddSeralizer(ModelSerializer):
    class Meta:
        model=Addpagelist
        fields='__all__'