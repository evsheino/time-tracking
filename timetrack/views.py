from django.http import HttpResponse
from django.shortcuts import render
from timetrack.models import WorkEntry
from timetrack.forms.model_forms import WorkEntryForm
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory

@login_required
def index(request):
    return render(request, 'timetrack/index.html')

@login_required
def show_entry(request, work_entry_id):
    return HttpResponse("WorkEntry %s" % work_entry_id)

@login_required
def new_entry(request):
    f = WorkEntryForm()
    return render(request, 'timetrack/new.html', { 'form': f })

@login_required
def create_entry(request):
    try:
        work_entry = WorkEntry(request.POST[''])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
