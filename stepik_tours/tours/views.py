from django.shortcuts import render
from django.views import View
from tours.data import title, subtitle, description, departures, tours
from django.http import Http404


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context={
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departures': departures,
                'tours': tours,
            }
        )


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        if departure in departures:
            return render(
                request, 'tours/departure.html', context={
                    'title': title,
                    'departures': departures,
                    'departure': departures[departure],
                }
            )
        else:
            raise Http404


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        if id in tours:
            return render(
                request, 'tours/tour.html', context={
                    'title': title,
                    'departures': departures,
                }
            )
        else:
            raise Http404
