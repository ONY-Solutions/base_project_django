from abc import ABC


class BaseRepository(ABC):

    def __init__(self, Model) -> None:
        self.Model = Model

    def get_all(self, visible=True):
        return self.Model.objects.filter(visible=visible)

    def get_by_id(self, pk):
        return self.Model.objects.get(id=pk)

    def create(self, data):
        return self.Model.objects.create(**data)

    def update(self, pk, data):
        query = self.Model.objects.get(id=pk)
        for key, value in data.items():
            setattr(query, key, value)
        query.save()
        return query

    def delete(self, pk):
        query = self.Model.objects.get(id=pk, visible=True)
        query.visible = False
        query.save()
        return query
