import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from pk.models import Pack, Item


class PackType(DjangoObjectType):
    class Meta:
        model = Pack
        fields = ("id", "name", "user", "items")


class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ("id", "name")


class Query(graphene.ObjectType):
    packs_by_username = graphene.List(PackType, username=graphene.String(required=True))

    def resolve_packs_by_username(root, info, username):
        # We can easily optimize query count in the resolve method
        # user = User.objects.get_by_natural_key(username)
        return list(Pack.objects.filter(user__username=username).all())


schema = graphene.Schema(query=Query)
