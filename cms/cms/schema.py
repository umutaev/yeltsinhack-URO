import graphene
from graphene_django import DjangoObjectType

from camps.models import CampModel


class CampType(DjangoObjectType):
    class Meta:
        model = CampModel
        fields = ("id", "start_date", "end_date", "title", "type", "description")
    
    picture_url = graphene.String()

    def resolve_picture_url(self, info):
        if self.picture:
            return self.picture.url


class Query(graphene.ObjectType):
    all_camps = graphene.List(CampType)
    __doc__ = "Base query"

    def resolve_all_camps(self, info):
        return CampModel.objects.all()


schema = graphene.Schema(query=Query)
