import pytest

from app.test_utils import make_post_req_to_server
from app.utils import apply_discount, apply_state_taxes


@pytest.mark.parametrize('money_amount, expected_result',
                        [(50000, 50000), (100000, 97000), (150000, 145500), (600000, 570000),
                        (800000, 744000), (1000000, 900000), (5000000, 4250000)])
def test_apply_discount(money_amount: int, expected_result: int):
    assert int(apply_discount(money_amount)) == expected_result


@pytest.mark.parametrize('state_code,expected_result', [('NV', 1080)])
def test_apply_taxes(state_code, expected_result):
    __money_amount = 1000
    assert apply_state_taxes(__money_amount, state_code) == expected_result


@pytest.mark.parametrize('items_count,price,state_code,result',
                        [(1, 100000, 'TX', 103062), (10, 60000, 'AL', 592800)])
def test_calculate(items_count: int, price: int, state_code: str, result: int):
    response = make_post_req_to_server('/api/calculate', json={'items_count': items_count,
                                                           'price': price, 'state_code': state_code})

    assert response.status_code == 200
    assert 'cost_after_taxes' in response.json and response.json['cost_after_taxes'] == result

