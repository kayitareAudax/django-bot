from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(["GET"])
def getData(request):
    data={
        "name":"John",
        "age":23,
        "city":"New York"
    }
    return Response(data)
