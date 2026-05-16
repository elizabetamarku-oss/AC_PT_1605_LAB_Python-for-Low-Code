🛍️ Product Generator — Refactored Python Project

This project generates structured product listings (title, description, features, keywords) using product metadata and images.
It is a refactored version of earlier labs (M1.05 and M1.06), redesigned to follow professional software engineering practices:

Modular architecture

Helper functions
Clear separation of concerns
Robust error handling
Testable components
No silent failures

The project uses a HuggingFace dataset of fashion product images and prepares prompts for an LLM to generate product descriptions.

📁 Project Structure

product-generator/
│
├── .env                     # API keys (not committed)
├── .gitignore               # Ignore env, cache, outputs
├── README.md                # This file
│
├── notebooks/
│   └── 01_refactor_lab.ipynb   # Notebook for testing & exploration
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Load dataset (HF or fallback)
│   ├── image_utils.py          # Image loading + base64 encoding
│   ├── prompt_builder.py       # Prompt creation
│   ├── model_api.py            # API wrapper (placeholder or real)
│   ├── processor.py            # Process a single product
│   └── batch_runner.py         # Process multiple products
│
└── main.py                     # Entry point to run the full pipeline

🚀 Features

- Loads product data from HuggingFace or local fallback
- Extracts and encodes product images
- Builds structured prompts for LLMs
- Processes products individually or in batches
- Captures and reports errors with full traceback
- Saves generated listings to JSON

🔧 Installation

1. Clone the repository:
   git clone <your-repo-url>
cd product-generator

3. Create a virtual environment:
   python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

4. Install dependencies:
   pip install -r requirements.txt

🔐 Environment Variables
Create a .env file in the project root:

OPENAI_API_KEY=your_key_here

This file is ignored by Git.

▶️ Running the Project

Run the full batch pipeline:
python main.py

This will:

- Load the dataset
- Process each product
- Generate prompts
- Call the model (placeholder or real)
- Save results to product_listings.json

🧪 Using the Notebook

The notebook is for testing only.

It should contain:

- A clean import cell
- A dataset preview
- A single‑product test
- A batch test

It should not contain business logic or helper functions.

🧱 Error Handling

This project follows the rule: Do not fail silently — fail loudly and show WHERE the error occurred.

Every module raises errors with:

- Function name
- Product ID
- Full traceback
- Contextual message

📌 Notes

- The Edge browser metadata block that sometimes appears in notebooks is not part of this project and should be deleted whenever it appears.
- All real logic lives in src/.
- The notebook is only a sandbox for exploration.


