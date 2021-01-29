from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from .parser import post_parse_and_create

class PostsList(APIView):
    limit = 30
    model = Post

    def get(self, request, format=None):
        # post_parse_and_create()
        offset = request.query_params.get('offset', 0)
        limit = request.query_params.get('limit', 5)
        order = request.query_params.get('order', '-pk')
        fields = [field.name for field in self.model._meta.get_fields()]
        if order.strip('-') not in fields:
            order = '-pk'

        try:
            offset = int(offset)
            limit = int(limit)
        except ValueError as e:
            data = {'value_error': 'offset or limit must be int values'}
        else:
            if limit > self.limit:
                data = {'limit_error': f'limit can\'t be > {self.limit}'}
            else:
                posts = self.model.objects.all().order_by(order)[int(offset):int(offset) + int(limit)]
                serializer = PostSerializer(posts, many=True)
                data = serializer.data
        return Response(data)

