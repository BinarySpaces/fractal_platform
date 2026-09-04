from abc import ABC, abstractmethod

from app.models import BaseParams


class BaseFractalGenerator(ABC):

    @abstractmethod
    def generate(self, params: BaseParams) -> str:
        """Генерирует фрактал и возвращает URL к изображению"""
        pass
