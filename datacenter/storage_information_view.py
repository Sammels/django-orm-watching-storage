from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.format_utils import format_duration


def storage_information_view(request):
    storage_visits = Visit.objects.filter(leaved_at=None)
    serialized_visits = []
    for visit in storage_visits:
        local_time = localtime(visit.entered_at).strftime("%Y-%m-%d %H:%M:%S")
        duration = format_duration(visit.get_duration)
        non_closed_visits = {
                'who_entered': visit.passcard.owner_name,
                'entered_at': local_time,
                'duration': duration,
                'is_strange': visit.is_visit_long
        }
        serialized_visits.append(non_closed_visits)

    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
