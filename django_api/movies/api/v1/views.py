from django.contrib.postgres.aggregates import ArrayAgg
from django.db import connection
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView

from movies.models import FilmWork, PersonRole


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']

    def get_queryset(self):
        get_genres = ArrayAgg('genres__name', distinct=True)
        get_actors = ArrayAgg(
            'person__full_name',
            filter=Q(film_person__role__exact=PersonRole.ACTOR),
            distinct=True,
        )
        get_directors = ArrayAgg(
            'person__full_name',
            filter=Q(film_person__role__exact=PersonRole.DIRECTOR),
            distinct=True,
        )
        get_writes = ArrayAgg(
            'person__full_name',
            filter=Q(film_person__role__exact=PersonRole.SCREENWRITER),
            distinct=True,
        )
        queryset = FilmWork.objects.prefetch_related(
            'genres',
            'film_person',
        ).values(
            'id', 'title', 'description', 'creation_date', 'rating', 'type'
        ).annotate(
            genres=get_genres, actors=get_actors, directors=get_directors, writers=get_writes,
        )
        return queryset

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        next_page = page.next_page_number() if page.has_next() else None
        prev_page = page.previous_page_number() if page.has_previous() else None
        context = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": prev_page,
            "next": next_page,
            'results': list(queryset),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs):
        return self.object
