from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.format_utils import format_duration


def storage_information_view(request):
    unclose_visits = Visit.objects.filter(leaved_at=None)
    entered_list = []
    for visits in unclose_visits:
            local_time = localtime(visits.entered_at).strftime("%Y-%m-%d %H:%M:%S")
            duration = format_duration(visits.get_duration)

            non_closed_visits = {
                    'who_entered': visits.passcard.owner_name,
                    'entered_at': local_time,
                    'duration': duration,
            }
            entered_list.append(non_closed_visits)

    context = {
        'non_closed_visits': entered_list,
    }
    return render(request, 'storage_information.html', context)
