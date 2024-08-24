from abc import ABC
from django.db import models

class BaseRepository(ABC):

    def __init__(self, Model: models.Model) -> None:
        self.Model = Model

    def get_all(self, visible=True):
        return self.Model.objects.filter(visible=visible)

    def filter_custom(self, **kwargs):
        return self.Model.objects.filter(**kwargs)

    def complex_filters(self, **kwargs):
        model = self.Model.objects

        for k in kwargs.keys():
            v = kwargs.get(k, None)

            if not v:
                continue

            if k == "filter":
                filtro = models.Q()

                for fk in v.keys():
                    filtro &= models.Q(**{fk: v.get(fk, None)})

                model = model.filter(filtro)
            elif k == "related":
                model = model.select_related(*v)
            elif k == "prefetch":
                model = model.prefetch_related(*v)
            elif k == "annotate":
                annotate = {}
                for fk in v.keys():
                    annotate[fk] = v.get(fk, None)
                model = model.annotate(**annotate)
            elif k == "aggregate":
                model.aggregate(*v)
            elif k == "values":
                model = model.values(*v)
            elif k == "defer":
                model = model.defer(*v)

        return model

    def get_by_id(self, pk):
        return self.Model.objects.get(id=pk)

    def create(self, data):
        return self.Model.objects.create(**data)

    def update(self, pk, data):
        query = self.Model.objects.get(id=pk, visible=True)
        for key, value in data.items():
            setattr(query, key, value)
        query.save()
        return query

    def delete(self, pk):
        query = self.Model.objects.get(id=pk, visible=True)
        query.visible = False
        query.save()
        return query
