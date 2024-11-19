from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MemberSerializer
from .models import Member


# Create your views here.
class Member_API(APIView):
    def get(self, request, pk=None):
        if pk == None:
            obj = Member.objects.all()
            serializer = MemberSerializer(obj, many=True)
            return Response(data=serializer.data)
        objs = get_object_or_404(Member, id=pk)
        serializer = MemberSerializer(objs)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data={"msg": "Data is Invalid"})

    def delete(self, request, pk):
        obj = get_object_or_404(Member, id=pk)
        obj.delete()
        return Response(data={"msg": "Data Deleted successfully"})

    def put(self, request, pk):
        obj = Member.objects.get(id=pk)
        serializer = MemberSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data={"msg": "Data is not valid"})

