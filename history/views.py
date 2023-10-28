import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import SearchHistory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SearchHistory
from django.http import HttpResponseBadRequest, HttpResponseRedirect

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
    return render(request, 'history.html', {'histories': histories})

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