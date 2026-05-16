def create_product_listing_prompt(
    product_name: str,
    price: float,
    category: str,
    additional_info: str | None = None,
) -> str:
    """
    Build the prompt for the product listing generation.
    Pure function: no side effects, no external calls.
    """
    extra = f"- Additional Info: {additional_info}" if additional_info else ""

    prompt = f"""
You are an expert e-commerce copywriter. Analyze the product image and create a compelling product listing.

Product Information:
- Name: {product_name}
- Price: ${price:.2f}
- Category: {category}
{extra}

Please create a professional product listing that includes:

1. **Product Title** (catchy, SEO-friendly, 60 characters max)
2. **Product Description** (detailed, 150–200 words)
3. **Key Features** (bullet points, 5–7 items)
4. **SEO Keywords** (comma-separated, 10–15 relevant keywords)

Format your response as JSON:
{{
    "title": "Product title here",
    "description": "Full description here",
    "features": ["Feature 1", "Feature 2"],
    "keywords": "keyword1, keyword2"
}}
"""
    return prompt