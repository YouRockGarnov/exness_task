

def apply_discount(money_amount: int) -> float:
    threshold_to_discount = (
        (100000, 0.03),
        (500000, 0.05),
        (700000, 0.07),
        (1000000, 0.1),
        (5000000, 0.15)
    )

    if money_amount < threshold_to_discount[0][0]:
        return money_amount

    def _apply_discount(discount: int, money_amount: int):
        return (1 - discount) * money_amount

    for i in range(len(threshold_to_discount)):
        if threshold_to_discount[i][0] > money_amount:
            return _apply_discount(threshold_to_discount[i-1][1], money_amount)

    return _apply_discount(threshold_to_discount[-1][1], money_amount)


def apply_state_taxes(money_amount: int, state_code: str) -> float:
    state_code_to_tax = {
        'UT': 0.0685,
        'NV': 0.08,
        'TX': 0.0625,
        'AL': 0.04,
        'CA': 0.0825
    }

    return (1 + state_code_to_tax[state_code]) * money_amount
