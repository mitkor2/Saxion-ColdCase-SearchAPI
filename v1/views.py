import requests
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import generics, filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.serializers import UserSerializer, GroupSerializer

from v1.models import Article
from v1.serializers import ArticleSerializer
import environ


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ['url', 'site', 'title', 'date', 'case', 'content']
    filter_backends = (filters.SearchFilter,)


class NewsApiView(APIView):
    def get(self, request, search=''):
        env = environ.Env()
        # reading .env file
        environ.Env.read_env()
        url = env("NEWSAPI_URL")
        if search:
            querystring = {"textFormat": "Raw", "safeSearch": "Off", "q": "Cold case " + search,
                           "freshness": "Month",
                           "CC": "NL"}
        else:
            querystring = {"textFormat": "Raw", "safeSearch": "Off", "q": "Cold case", "freshness": "Month",
                           "CC": "NL"}
        headers = {
            'x-bingapis-sdk': 'true',
            'x-rapidapi-key': env("RAPIDAPI_KEY"),
            'x-rapidapi-host': env("RAPIDAPI_HOST")
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return Response({'news': data['value']})
