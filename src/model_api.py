import json
import os
import traceback
from typing import Any, Dict

from dotenv import load_dotenv

load_dotenv()  # loads .env from project root


def call_model(prompt: str, image_b64: str) -> Dict[str, Any]:
    """
    Call the model with the given prompt and image.
    For now, returns a placeholder response.

    Replace this with your actual OpenAI API call.
    """
    try:
        # Example of where you'd use your key:
        # api_key = os.getenv("OPENAI_API_KEY")
        # assert api_key, "OPENAI_API_KEY is not set in .env"

        # TODO: Replace with real API call.
        # This is just a stub to keep architecture clean.
        response = {
            "title": "Example title",
            "description": "Example description",
            "features": ["Example feature"],
            "keywords": "example, keywords",
        }

        # Optionally validate structure here
        if not isinstance(response, dict):
            raise ValueError("Model response is not a dict.")

        return response

    except Exception as e:
        tb = traceback.format_exc()
        raise RuntimeError(
            f"[call_model] Failed to call model. Error: {e}\nTraceback:\n{tb}"
        ) from e