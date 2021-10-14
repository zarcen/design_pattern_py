from strategy.shipping_cost import *
from strategy.strategies import *

def costOf(order: Order, strategy: AbsStrategy):
    cost_calculator = ShippingCost(strategy)
    return cost_calculator.shipping_cost(order)

def test_fedex():
    assert 2.0 == costOf(Order(2.0), FedExStrategy())

def test_ups():
    assert 6.0 == costOf(Order(2.0), UPSStrategy())

def test_postal():
    assert 7.0 == costOf(Order(2.0), PostalStrategy())