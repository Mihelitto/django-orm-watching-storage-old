from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    visitors = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visitor in visitors:
        non_closed_visits.append(
            {
                "who_entered": visitor.passcard,
                "entered_at": localtime(visitor.entered_at),
                "duration": visitor.format_duration(),
                "is_strange": visitor.is_visit_long(),
            }
        )
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
