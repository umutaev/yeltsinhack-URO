import graphene
from graphene_django import DjangoObjectType

from camps.models import CampModel
from programms.models import ProgrammModel


class CampType(DjangoObjectType):
    class Meta:
        model = CampModel
        fields = ("id", "start_date", "end_date", "title", "type", "description")
    
    picture_url = graphene.String()

    def resolve_picture_url(self, info):
        if self.picture:
            return self.picture.url


class ProgrammType(DjangoObjectType):
    class Meta:
        model = ProgrammModel
        fields = ("id", "start_date", "end_date", "title", "type", "description")
    
    picture_url = graphene.String()

    def resolve_picture_url(self, info):
        if self.picture:
            return self.picture.url

class Query(graphene.ObjectType):
    all_camps = graphene.List(CampType)
    all_programms = graphene.List(ProgrammType)
    __doc__ = "Base query"

    def resolve_all_camps(self, info):
        return CampModel.objects.all()
    
    def resolve_all_programms(self, info):
        return ProgrammModel.objects.all()


schema = graphene.Schema(query=Query)
