import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from pk.models import Pack, Item


class PackType(DjangoObjectType):
    class Meta:
        model = Pack
        fields = ("id", "name", "items")


class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ("id", "name")


class Query(graphene.ObjectType):
    packs = graphene.List(PackType)

    def resolve_packs(self, info):
        # We can easily optimize query count in the resolve method
        # FIXME: load username by auth token
        username = 'nanfang'
        return list(Pack.objects.filter(user__username=username).all())


schema = graphene.Schema(query=Query)
