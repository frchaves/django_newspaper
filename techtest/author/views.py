from django.shortcuts import render

import json
from marshmallow import ValidationError
from django.views import View
from django.http import JsonResponse

from techtest.articles.models import Article
from techtest.author.models import Author
from techtest.articles.schemas import ArticleSchema
from techtest.author.schemas import AuthorSchema
from techtest.utils import json_response


# from .models import Article, Author, Region
# from .schemas import ArticleSchema, AuthorSchema, RegionSchema

# Create your views here.
class AuthorsListView(View):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        author_schema = AuthorSchema(many=True)
        serialized_authors = author_schema.dump(authors)
        return JsonResponse(serialized_authors, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            author_data = json.loads(request.body)
            author_schema = AuthorSchema()
            author = author_schema.load(author_data)
            author.save()
            serialized_author = author_schema.dump(author)
            return JsonResponse(serialized_author, status=201)
        except ValidationError as e:
            return JsonResponse(e.messages, status=400)


class AuthorView(View):
    def dispatch(self, request, author_id, *args, **kwargs):
        try:
            self.author = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return JsonResponse({"error": "No Author matches the given query"}, status=404)
        self.data = request.body and dict(json.loads(request.body), id=self.author.id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        author_schema = AuthorSchema()
        serialized_author = author_schema.dump(self.author)
        return JsonResponse(serialized_author)

    def put(self, request, *args, **kwargs):
        try:
            author_schema = AuthorSchema()
            self.author = author_schema.load(self.data)
            self.author.save()
            serialized_author = author_schema.dump(self.author)
            return JsonResponse(serialized_author)
        except ValidationError as e:
            return JsonResponse(e.messages, status=400)

    def delete(self, request, *args, **kwargs):
        self.author.delete()
        return JsonResponse({})
