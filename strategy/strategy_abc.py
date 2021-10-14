from abc import ABC, abstractmethod

class AbsStrategy(ABC):

    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost """
        return order.flat_fee