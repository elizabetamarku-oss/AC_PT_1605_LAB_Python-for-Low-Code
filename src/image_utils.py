import base64
from io import BytesIO
from pathlib import Path

import pandas as pd
from PIL import Image


def load_image_from_row(row: pd.Series) -> Image.Image:
    """
    Load a PIL image from a dataset row.

    For the HuggingFace dataset, the 'image' field is already a PIL Image.
    For local fallback, we expect 'image_path'.
    """
    try:
        if "image" in row and isinstance(row["image"], Image.Image):
            return row["image"].convert("RGB")

        if "image_path" in row and row["image_path"]:
            path = Path(row["image_path"])
            if not path.exists():
                raise FileNotFoundError(f"Image file not found: {path}")
            return Image.open(path).convert("RGB")

        raise ValueError("Row does not contain a valid image or image_path.")
    except Exception as e:
        product_id = row.get("id", "unknown")
        raise RuntimeError(
            f"[load_image_from_row] Failed to load image for row id={product_id}: {e}"
        ) from e


def encode_pil_image_to_base64(pil_image: Image.Image) -> str:
    """
    Encode a PIL image to a base64 string (JPEG).
    """
    buffer = BytesIO()
    pil_image.save(buffer, format="JPEG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return encoded