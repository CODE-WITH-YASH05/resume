from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from accounts.models.about_models import AboutUs
from accounts.serializers import AboutUsSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def about_us_view(request):

    if request.method == 'GET':
        about = AboutUs.objects.first()
        serializer = AboutUsSerializer(about)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)