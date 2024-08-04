from abc import ABC, abstractmethod


class BaseService(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, pk):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
