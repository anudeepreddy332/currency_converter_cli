import argparse
from currency import Currency

def main():
    parser = argparse.ArgumentParser(
        description="Currency Converter"
    )
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "--list",
        action="store_true",
        help="List of available currency codes"
    )
    group.add_argument(
        "--history",
        action="store_true",
        help="Show conversion history"
    )
    group.add_argument(
        "--amount",
        type=float,
        help="Amount to convert (required if not using --list)"
    )
    parser.add_argument(
        "--from_currency",
        type=str,
        help="Input 'from' currency"
    )
    parser.add_argument(
        "--to_currency",
        type=str,
        help="Input 'to' currency"
    )

    args = parser.parse_args()

    if args.list:
        Currency.list_currencies()
        return

    if args.history:
        Currency(0,"usd","inr").show_history()
        return

    if args.amount is None or args.from_currency is None or args.to_currency is None:
        parser.error("All of --amount, --from_currency, and --to_currency are required unless using --list")

    currency = Currency(args.amount, args.from_currency, args.to_currency)
    result = currency.convert()

    if result is not None:
        print(f"{args.amount} {args.from_currency.upper()} = "
              f"{result:.2f} {args.to_currency.upper()}")
    else:
        print("[INFO] Conversion failed due to error above.")

if __name__ == "__main__":
    main()