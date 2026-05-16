import traceback
from typing import Any, Dict

import pandas as pd

from .image_utils import load_image_from_row, encode_pil_image_to_base64
from .model_api import call_model
from .prompt_builder import create_product_listing_prompt


def process_product_row(row: pd.Series) -> Dict[str, Any]:
    """
    Process a single product row:
    - load image
    - encode image
    - build prompt
    - call model
    Returns a dict with the final listing.
    """
    product_id = row.get("id", "unknown")
    product_name = row.get("productDisplayName", "Unknown Product")

    try:
        pil_img = load_image_from_row(row)
        img_b64 = encode_pil_image_to_base64(pil_img)

        prompt = create_product_listing_prompt(
            product_name=product_name,
            price=float(row.get("price", 0.0)),
            category=row.get("masterCategory", "Unknown"),
            additional_info=row.get("subCategory"),
        )

        listing = call_model(prompt, img_b64)

        return {
            "id": product_id,
            "name": product_name,
            "prompt": prompt,
            "image_base64": img_b64,
            "listing": listing,
        }

    except Exception as e:
        tb = traceback.format_exc()
        raise RuntimeError(
            f"[process_product_row] Failed for product id={product_id}, "
            f"name={product_name}. Error: {e}\nTraceback:\n{tb}"
        ) from e