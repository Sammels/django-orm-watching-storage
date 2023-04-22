from datacenter.models import Passcard
from django.utils.timezone import localtime
from django.shortcuts import render, get_object_or_404

from datacenter.format_utils import format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = passcard.visit_set.all()
    entered_list = []
    for visit in visits:
        entered_time = localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M')
        duration = format_duration(visit.get_duration)
        serialized_visit = {
            'entered_at': entered_time,
            'duration': duration,
            'is_strange': visit.is_visit_long
        }
        entered_list.append(serialized_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': entered_list
    }
    return render(request, 'passcard_info.html', context)
