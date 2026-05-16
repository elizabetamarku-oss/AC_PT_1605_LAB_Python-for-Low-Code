from pathlib import Path

import pandas as pd
from datasets import load_dataset


DATASET_NAME = "ashraq/fashion-product-images-small"
DATASET_SPLIT = "train[:100]"


def load_products_dataset(max_products: int | None = None) -> pd.DataFrame:
    """
    Load the products dataset from HuggingFace.
    Falls back to a small local example if loading fails.
    Returns a pandas DataFrame.
    """
    print("Loading product dataset...")
    try:
        dataset = load_dataset(DATASET_NAME, split=DATASET_SPLIT)
        df = pd.DataFrame(dataset)  # type: ignore

        if max_products is not None:
            df = df.iloc[:max_products].copy()

        print(f"Loaded {len(df)} products from HuggingFace.")
        print(f"Columns: {df.columns.tolist()}")
        return df

    except Exception as e:
        print("✗ Failed to load HuggingFace dataset.")
        print(f"  Error: {e}")
        print("→ Falling back to local example data.")

        products_data = [
            {
                "id": 1,
                "productDisplayName": "Wireless Headphones",
                "price": 79.99,
                "masterCategory": "Electronics",
                "subCategory": "Headphones",
                "image_path": "images/product1.jpg",
            }
        ]
        df = pd.DataFrame(products_data)
        print(f"Loaded {len(df)} local products.")
        return df