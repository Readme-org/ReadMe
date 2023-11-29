import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import SearchHistory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SearchHistory
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.core import serializers

@login_required
def history(request):
    if request.method == 'POST':
        history_id = request.POST.get('history_id')
        action = request.POST.get('action')

        if action == 'delete':
            SearchHistory.objects.filter(id=history_id).delete()
            messages.success(request, 'History deleted successfully!')
        elif action == 'edit':
            is_important = request.POST.get('is_important') == 'on'
            tag = request.POST.get('tag')
            SearchHistory.objects.filter(id=history_id).update(
                is_important=is_important, tag=tag)
            messages.success(request, 'History updated successfully!')

        return redirect('history:history')

    histories = SearchHistory.objects.filter(user=request.user)

    context = {
        'histories': histories,
        'name': request.user.username
    }

    return render(request, 'history.html', context)

def add_search_history(request):
    if request.method != 'POST':
        return HttpResponseForbidden('Invalid Method.')

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON.')

    query = data.get("query")
    if not query:
        return HttpResponseBadRequest('Query is required.')

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    history = SearchHistory(user=request.user, query=query)
    history.save()

    return HttpResponse(status=201)

@login_required
def delete_history_ajax(request):
    if request.method == 'POST':
        history_id = request.POST.get('history_id')
        history = SearchHistory.objects.filter(id=history_id)
        if history.exists():
            history.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest('Invalid history ID.')
    return HttpResponseForbidden('Invalid method.')

def show_history_json(request):
    data = history.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")