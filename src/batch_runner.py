from typing import Any, Dict, List, Tuple

import pandas as pd

from .processor import process_product_row


def process_products_batch(df: pd.DataFrame) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Process all products in the DataFrame.
    Returns (results, errors).
    """
    results: List[Dict[str, Any]] = []
    errors: List[Dict[str, Any]] = []

    total = len(df)
    print(f"Starting batch processing for {total} products...\n")

    for idx, (_, row) in enumerate(df.iterrows(), start=1):
        print(f"Processing product {idx}/{total} (id={row.get('id')})")
        try:
            result = process_product_row(row)
            results.append(result)
            print("  [OK] Success")
        except Exception as e:
            error_info = {
                "index": idx,
                "id": row.get("id"),
                "name": row.get("productDisplayName"),
                "error": str(e),
            }
            errors.append(error_info)
            print("  [ERROR] Error while processing product.")
            print(f"    {e}\n")

    print(f"Batch complete. Success: {len(results)}, Errors: {len(errors)}")
    return results, errors