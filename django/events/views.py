from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import permission_required

from .models import Event, NewEventForm, EditEventForm


# Create your views here.
def index(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, "events/index.html", context=context)


def details(request, event_id):
    context = {
        'event': get_object_or_404(Event, pk=event_id)
    }
    return render(request, "events/details.html", context=context)


@permission_required('events.add_event', raise_exception=True)
def new(request):
    if (request.method == 'POST'):
        form = NewEventForm(request.POST, request.FILES)
        if (form.is_valid()):
            data = form.cleaned_data
            event = Event(title=data.get('title'),
                          short_desc=data.get('short_desc'),
                          long_desc=data.get('long_desc'),
                          start_time=data.get('start_time'),
                          end_time=data.get('end_time'),
                          banner=data.get('banner'))
            event.save()
            return redirect('events:details', event_id=event.id)
    else:
        form = NewEventForm()
    return render(request, 'misc/forms.html', {'form': form,
                                               'target': 'events:new',
                                               'submit': 'Create Event',
                                               'title': 'New Event'})
    pass


@permission_required('events.change_event', raise_exception=True)
def edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if (request.method == 'POST'):
        form = EditEventForm(request.POST, request.FILES)
        if (form.is_valid()):
            data = form.cleaned_data

            event.title = data.get('title')
            event.short_desc = data.get('short_desc')
            event.long_desc = data.get('long_desc')
            event.start_time = data.get('start_time')
            event.end_time = data.get('end_time')

            event.save()
            return redirect('events:details', event_id=event.id)
    else:
        data = {
            'title': event.title,
            'short_desc': event.short_desc,
            'long_desc': event.long_desc,
            'start_time': event.start_time,
            'end_time': event.end_time,
        }
        file_data = {
            'banner': event.banner,
        }
        form = EditEventForm(data, file_data)
    return render(request, 'misc/forms.html', {'form': form,
                                               'target': 'events:edit',
                                               'argument': event_id,
                                               'submit': 'Update Event',
                                               'title': 'Edit Event'})
    pass
