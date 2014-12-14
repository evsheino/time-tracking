from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from timetrack.models import WorkEntry
from timetrack.forms.model_forms import WorkEntryForm
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory

@login_required
def index(request):
    entries = WorkEntry.objects.filter(user=request.user).order_by('-date')[:10]
    context = {'entries': entries}
    return render(request, 'timetrack/index.html', context)

@login_required
def show_entry(request, work_entry_id):
    entry = get_object_or_404(WorkEntry, pk=work_entry_id)

    return render(request, 'timetrack/show.html', { 'entry': entry })

@login_required
def new_entry(request):
    if request.method == 'POST':
        f = WorkEntryForm(request.POST)
        if f.is_valid():
            work_entry = f.save(commit=False)
            work_entry.user = request.user
            work_entry.save()
            return HttpResponseRedirect(reverse('timetrack:show_entry', args=(work_entry.id,)))
        return render(request, 'timetrack/new.html', { 'form': f })

    else:
        f = WorkEntryForm()
        return render(request, 'timetrack/new.html', { 'form': f })
