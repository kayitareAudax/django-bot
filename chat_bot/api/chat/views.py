from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Chat, Page, Document, Session
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@require_http_methods(["POST"])
@permission_classes([IsAuthenticated])
def create_chat(request):
    data=json.loads({request.body,request.user.id})
    chat = Chat.objects.create(**data)
    return JsonResponse({'id': chat.id, 'message': chat.message}, status=201)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def read_chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id, session=request.user)
    return JsonResponse({'id': chat.id, 'message': chat.message})

@csrf_exempt
@require_http_methods(["PUT"])
def update_chat(request, chat_id):
    data = json.loads(request.body)
    chat = get_object_or_404(Chat, id=chat_id)
    for key, value in data.items():
        setattr(chat, key, value)
    chat.save()
    return JsonResponse({'id': chat.id, 'message': chat.message})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    chat.delete()
    return JsonResponse({'message': 'Chat deleted'}, status=204)

@csrf_exempt
@require_http_methods(["POST"])
def create_page(request):
    data = json.loads(request.body)
    page = Page.objects.create(**data)
    return JsonResponse({'id': page.id, 'title': page.title}, status=201)

@require_http_methods(["GET"])
def read_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return JsonResponse({'id': page.id, 'title': page.title})

@csrf_exempt
@require_http_methods(["PUT"])
def update_page(request, page_id):
    data = json.loads(request.body)
    page = get_object_or_404(Page, id=page_id)
    for key, value in data.items():
        setattr(page, key, value)
    page.save()
    return JsonResponse({'id': page.id, 'title': page.title})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    page.delete()
    return JsonResponse({'message': 'Page deleted'}, status=204)

@csrf_exempt
@require_http_methods(["POST"])
def create_document(request):
    data = json.loads(request.body)
    document = Document.objects.create(**data)
    return JsonResponse({'id': document.id, 'name': document.name}, status=201)

@require_http_methods(["GET"])
def read_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    return JsonResponse({'id': document.id, 'name': document.name})

@csrf_exempt
@require_http_methods(["PUT"])
def update_document(request, document_id):
    data = json.loads(request.body)
    document = get_object_or_404(Document, id=document_id)
    for key, value in data.items():
        setattr(document, key, value)
    document.save()
    return JsonResponse({'id': document.id, 'name': document.name})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return JsonResponse({'message': 'Document deleted'}, status=204)

@csrf_exempt
@require_http_methods(["POST"])
def create_session(request):
    data = json.loads(request.body)
    session = Session.objects.create(**data)
    return JsonResponse({'id': session.id, 'user': session.user}, status=201)

@require_http_methods(["GET"])
def read_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    return JsonResponse({'id': session.id, 'user': session.user})

@csrf_exempt
@require_http_methods(["PUT"])
def update_session(request, session_id):
    data = json.loads(request.body)
    session = get_object_or_404(Session, id=session_id)
    for key, value in data.items():
        setattr(session, key, value)
    session.save()
    return JsonResponse({'id': session.id, 'user': session.user})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    session.delete()
    return JsonResponse({'message': 'Session deleted'}, status=204)