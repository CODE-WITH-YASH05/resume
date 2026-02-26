from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from accounts.serializers import SchoolSettingsSerializer
from rest_framework.permissions import IsAuthenticated

#login
@api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {"error": "Username and password required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Login Successful",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

    return Response(
        {"error": "Invalid Credentials"},
        status=status.HTTP_401_UNAUTHORIZED
    )

#logout 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def admin_logout(request):
    try:
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"message": "Logout successful"})
    except Exception as e:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    
#dashboard
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_dashboard(request):
    return Response({
        "message": "Welcome Admin Dashboard",
        "user": request.user.username
    })  
    
#add logo & name
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_school_settings(request):
    serializer = SchoolSettingsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)