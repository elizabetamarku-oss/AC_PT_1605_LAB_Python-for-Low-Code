# 🛍️ Product Generator — Refactored Python Project

A modular, production‑ready system for generating structured product listings using product metadata and images.
This project refactors earlier labs (M1.05 & M1.06) into a clean, testable, maintainable Python package.

# 📁 Project Structure

```
product-generator/
├── .env
├── .gitignore
├── README.md
│
├── notebooks/
│   └── 01_refactor_lab.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── image_utils.py
│   ├── prompt_builder.py
│   ├── model_api.py
│   ├── processor.py
│   └── batch_runner.py
│
└── main.py
```

# 🚀 Features

✔ Modular Architecture
Each responsibility lives in its own module (data_loader, image_utils, processor, etc.).

✔ Robust Error Handling
Every function raises clear, contextual errors with full tracebacks.

✔ Image Processing
Loads and encodes product images from HuggingFace or local fallback.

✔ Prompt Generation
Builds structured prompts for LLM‑based product description generation.

✔ Batch Processing
Processes hundreds of products with progress output and error tracking.

# 🔧 Installation

1. Clone the repository
```Code
git clone <your-repo-url>
cd product-generator
```

4. Create a virtual environment
```Code
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

5. Install dependencies
```Code
pip install -r requirements.txt
```

# 🔐 Environment Variables

Create a .env file in the project root:
```Code
OPENAI_API_KEY=your_key_here
This file is ignored by Git.
```

# ▶️ Running the Project

Run the full pipeline:
```Code
python main.py
```
This will:

✔ Load the dataset
✔ Process each product
✔ Build prompts
✔ Call the model (placeholder or real)
✔ Save results to product_listings.json

# 🧪 Using the Notebook

The notebook is for testing only.

## It should contain:

✔ Import cell
✔ Dataset preview
✔ Single‑product test
✔ Batch test

## It should not contain:

- Helper functions
- API logic
- Image processing logic
- Business logic

All real logic lives in src/.

# 🧱 Error Handling Philosophy

This project follows a strict rule: Do not fail silently — fail loudly and show WHERE the error occurred.

Every module raises errors with:

- Function name
- Product ID
- Full traceback
- Helpful context

# 📌 Notes

- The Edge browser metadata block that sometimes appears in notebooks is not part of this project and should be deleted whenever it appears.
- The src/ folder contains all real logic.
- The notebook is a sandbox for exploration, not the application.
