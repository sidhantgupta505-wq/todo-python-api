from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET', 'POST'])
def todo_list(request):

    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['PUT', 'PATCH', 'DELETE'])
def todo_detail(request, id):

    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=404)

    if request.method in ['PUT', 'PATCH']:
        serializer = TodoSerializer(
            todo,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        todo.delete()
        return Response({"message": "Todo deleted"})