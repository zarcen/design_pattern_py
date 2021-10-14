from strategy.strategy_abc import AbsStrategy

class Order:
    def __init__(self, fee=0):
        self.flat_fee = fee
        return

class ShippingCost(object):
    def __init__(self, strategy: AbsStrategy):
        self._strategy = strategy

    def shipping_cost(self, order: Order):
        return self._strategy.calculate(order)