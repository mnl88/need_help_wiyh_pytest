import pytest


# нужно как-то переделать тест, который ниже...
def test_that_not_works_correct(get_pairs_from_test_db):
    pairs = get_pairs_from_test_db
    for pair in pairs:
        assert pair[0] == pair[1]


"""
Прошу помочь написать тесты, которые бы сравнивали попарно значения в списке pairs
Ниже пример как +- она бы выглядела с параметризацией
"""


# это то, как бы я хотел, чтобы отрабатывали тесты, если бы я смог прокинуть значения из БД в параметры
@pytest.mark.parametrize('pair', [
    (('Nikita', 15), ('Nikita', 15)),
    (('Alex', 20), ('Alex', 21)),
    (('Maria', 25), ('Maria', 23)),
    (('Boris', 34), ('Boris', 34)),
    (('Liza', 35), ('Liza', 33))])
def test_simple_equals_in_pair(pair):
    assert pair[0] == pair[1]
