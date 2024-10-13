import pytest
from src import Products, Category


@pytest.fixture
def product_name():
    return Product("Джинсы", "черные, фасон MOM", 1990, 3)


@pytest.fixture
def category_name():
    return Category("Штаны", "Джинсы, спортивные штаны, брюки", ["Джинсы", "Брюки", "Спортивные Штаны"])


def test_product_init(product_name, category_name):
    assert product_name.name == "Джинсы"
    assert product_name.description == "черные, фасон MOM"
    assert product_name.price == 1990
    assert product_name.quantity == 3


def test_category_init(category_name):
    assert category_name.name == "Штаны"
    assert category_name.quantity == "Джинсы, спортивные штаны, брюки"
    assert category_name.products == ["Джинсы", "Брюки", "Спортивные штаны"]


def test_quantity_category():
    assert category_name.category_count == 1
    assert category_name.products_quantity == 3
