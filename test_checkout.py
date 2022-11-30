import pytest

from checkout import Checkout


@pytest.fixture
def checkout():
    return Checkout()


# def test_can_calculate_total(checkout):
#     checkout.add_item_price("widget", 100)
#     checkout.add_item("widget")
#     assert checkout.calculate_total() == 100


def test_can_get_correct_total_with_multiple_items(checkout):
    checkout.add_item_price("candy", 5)
    checkout.add_item_price("cereal", 15)
    checkout.add_item("cereal")
    checkout.add_item("candy")

    assert checkout.calculate_total() == 20
