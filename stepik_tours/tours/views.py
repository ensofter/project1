import random

from django.http import Http404
from django.shortcuts import render
from django.views import View
from tours.data import title, subtitle, description, departures, tours


class MainView(View):
    def get(self, request, *args, **kwargs):
        random_six_tours = random.sample(tours.items(), 6)
        return render(
            request, 'tours/index.html', context={
                'site_title': title,
                'site_subtitle': subtitle,
                'site_description': description,
                'menu': departures,
                'tours': random_six_tours,
            }
        )


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        if departure in departures:
            specific_tour = dict()
            prices = list()
            nights = list()
            for k, v in tours.items():
                if tours[k]['departure'] == departure:
                    specific_tour[k] = tours[k]
                    prices.append(tours[k]['price'])
                    nights.append(tours[k]['nights'])
            return render(
                request, 'tours/departure.html', context={
                    'site_title': title,
                    'menu': departures,
                    'departure_name': departures[departure],
                    'specific_tour': specific_tour,
                    'min_nights': min(nights),
                    'max_nights': max(nights),
                    'min_price': min(prices),
                    'max_price': max(prices),
                }
            )
        else:
            raise Http404


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        if id in tours:
            return render(
                request, 'tours/tour.html', context={
                    'site_title': title,
                    'menu': departures,
                    'tour_title': tours[id]['title'],
                    'starts': tours[id]['stars'],
                    'tour_country': tours[id]['country'],
                    'departure': departures[tours[id]['departure']],
                    'nights': tours[id]['nights'],
                    'tour_description': tours[id]['description'],
                    'picture': tours[id]['picture'],
                    'price': tours[id]['price'],
                }
            )
        else:
            raise Http404
