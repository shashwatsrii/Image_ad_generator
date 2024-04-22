def combine_product_and_background_prompt(product_name, background_prompt):
    """Combines product and background prompts into a single string.

    Args:
        product_name (str): Name of the product image.
        background_prompt (str): Textual description of the background.

    Returns:
        str: Combined prompt.
    """

    return f"A photorealistic image of a product image of {product_name} placed on {background_prompt}"
