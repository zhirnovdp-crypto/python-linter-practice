import argparse

from .pricing import total_price


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Рассчитать стоимость заказа по цене за единицу, "
            "количеству товаров и проценту скидки."
        ),
    )
    parser.add_argument("unit_price", type=int, help="цена за единицу в рублях")
    parser.add_argument("quantity", type=int, help="количество товаров")
    parser.add_argument("--discount", type=int, help="скидка в процентах")
    args = parser.parse_args()

    try:
        total = total_price(args.unit_price, args.quantity, args.discount)
    except ValueError as error:
        parser.error(str(error))
    print(total)


if __name__ == "__main__":
    main()
