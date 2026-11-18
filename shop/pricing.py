def total_price(
    unit_price: int, quantity: int, discount_percent: int | None = None
) -> int:
    """Рассчитать стоимость заказа в целых рублях."""
    if unit_price < 0 or quantity < 0:
        raise ValueError("Цена и количество должны быть неотрицательными")

    subtotal = unit_price * quantity
    if discount_percent is None:
        return subtotal

    if not 0 <= discount_percent <= 100:
        raise ValueError("Скидка должна быть от 0 до 100 процентов")

    return subtotal * (100 - discount_percent) // 100
