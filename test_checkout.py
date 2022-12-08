import pytest

from checkout import Checkout


class Fixtures:
    @pytest.fixture
    def checkout(self):
        return Checkout()


class TestRunner(Fixtures):
    def test_can_get_correct_total_with_multiple_items(self, checkout):
        checkout.add_item_price("candy", 5)
        checkout.add_item_price("cereal", 15)
        checkout.add_item("cereal")
        checkout.add_item("candy")

        assert checkout.calculate_total() == 20

    def test_can_add_discount_rule(self, checkout):
        checkout.add_discount("candy", 3, 2)

    def test_can_apply_discount_rule(self, checkout):
        checkout.add_item_price("candy", 10)
        checkout.add_discount("candy", 3, 2)
        checkout.add_item("candy")
        checkout.add_item("candy")
        checkout.add_item("candy")

        assert checkout.calculate_total() == 2

    def test_exception_with_bad_item(self, checkout):
        from checkout import NoPriceException
        with pytest.raises(NoPriceException):
            checkout.add_item("tacos")
