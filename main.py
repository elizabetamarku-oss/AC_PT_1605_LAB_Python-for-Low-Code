import json
from pathlib import Path

from src.data_loader import load_products_dataset
from src.batch_runner import process_products_batch


OUTPUT_PATH = Path("product_listings.json")


def main() -> None:
    products_df = load_products_dataset()

    results, errors = process_products_batch(products_df)

    # Save results
    try:
        OUTPUT_PATH.write_text(
            json.dumps(results, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"\nResults saved to: {OUTPUT_PATH.resolve()}")
    except Exception as e:
        print(f"[main] Failed to save results: {e}")

    if errors:
        print("\nErrors encountered:")
        for err in errors:
            print(f"- Index {err['index']}, id={err['id']}, name={err['name']}")
            print(f"  Error: {err['error']}\n")


if __name__ == "__main__":
    main()