def get_pay_amount():
    if is_dead:
        return dead_amount()
    if is_separated:
        return separated_amount()
    if is_retired:
        return retired_amount()
    return normal_pay_amount()
