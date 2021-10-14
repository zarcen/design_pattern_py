from strategy.strategy_abc import AbsStrategy
from strategy.shipping_cost import *

class FedExStrategy(AbsStrategy):
    def calculate(self, order: Order):
        return super().calculate(order)

class UPSStrategy(AbsStrategy):
    def calculate(self, order: Order):
        return order.flat_fee + 4.0

class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return order.flat_fee + 5.0