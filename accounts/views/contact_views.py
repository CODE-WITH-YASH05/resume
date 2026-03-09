from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import SchoolMap, ContactMessage
from accounts.models import EmailSettings
from accounts.utils.email_sender import send_dynamic_email


# Add School Contact Info MAP

@api_view(['POST'])
def add_school_contact(request):

    school = SchoolMap.objects.create(
        address=request.data.get("address"),
        phone=request.data.get("phone"),
        email=request.data.get("email"),
        map_embed=request.data.get("map_embed")
    )

    return Response({
        "message": "School contact saved"
    })


# Get School Contact Info MAP

@api_view(['GET'])
def contact_info(request):

    school = SchoolMap.objects.first()

    if not school:
        return Response({"error": "No contact info found"})

    return Response({
        "address": school.address,
        "phone": school.phone,
        "email": school.email,
        "map": school.map_embed
    })


# Contact Form Submit


@api_view(['POST'])
def contact_submit(request):

    name = request.data.get("name")
    email = request.data.get("email")
    phone = request.data.get("phone")
    message = request.data.get("message")

    ContactMessage.objects.create(
        name=name,
        email=email,
        phone=phone,
        message=message
    )

    # send email
    email_text = f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""  
# email settings database se
    config = EmailSettings.objects.first()

    # email send
    send_dynamic_email(
        "New Contact Message",
        email_text,
        config.email_host_user
    )

    return Response({
        "message": "Message sent successfully"
    })

#list contact form
@api_view(['GET'])
def contact_messages(request):

    messages = ContactMessage.objects.all()

    data = []

    for m in messages:
        data.append({
            "id": m.id,
            "name": m.name,
            "email": m.email,
            "phone": m.phone,
            "message": m.message
        })

    return Response(data)


# ADD EMAIL  SETTINGS
@api_view(['POST'])
def add_email_settings(request):

    email = EmailSettings.objects.create(
        email_host=request.data.get("email_host"),
        email_port=request.data.get("email_port"),
        email_host_user=request.data.get("email_host_user"),
        email_host_password=request.data.get("email_host_password"),
        use_tls=request.data.get("use_tls")
    )

    return Response({
        "message": "Email settings added",
        "id": email.id
    })


# GET EMAIL SETTINGS
@api_view(['GET'])
def get_email_settings(request):

    email = EmailSettings.objects.first()

    return Response({
        "email_host": email.email_host,
        "email_port": email.email_port,
        "email_host_user": email.email_host_user,
        "use_tls": email.use_tls
    })


# UPDATE EMAIL SETTINGS
@api_view(['PUT'])
def update_email_settings(request, id):

    email = EmailSettings.objects.get(id=id)

    email.email_host = request.data.get("email_host", email.email_host)
    email.email_port = request.data.get("email_port", email.email_port)
    email.email_host_user = request.data.get("email_host_user", email.email_host_user)
    email.email_host_password = request.data.get("email_host_password", email.email_host_password)
    email.use_tls = request.data.get("use_tls", email.use_tls)

    email.save()

    return Response({
        "message": "Email settings updated"
    })
    
@api_view(['DELETE'])
def delete_email_settings(request, id):

    try:
        email = EmailSettings.objects.get(id=id)
    except EmailSettings.DoesNotExist:
        return Response({"error": "Facility not found"})

    email.delete()

    return Response({
        "message": "EmailSettings deleted"
    })