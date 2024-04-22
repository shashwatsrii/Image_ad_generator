from models.stable_diffusion import StableDiffusionGenerator
from utils.image_utils import resize_image, save_image
from utils.prompt_utils import combine_product_and_background_prompt
import config
import os

def generate_ad_image(product_image, background_prompts):
    """Generates advertisement images for a product with different backgrounds.

    Args:
        product_image (str): Path to the product image file.
        background_prompts (list): List of text prompts for different backgrounds.

    Returns:
        None
    """

    # Load Stable Diffusion model
    generator = StableDiffusionGenerator(config.MODEL_NAME)

    # Load and resize product image
    try:
        product_img = Image.open(os.path.join(config.INPUT_PRODUCT_DIR, product_image))
        product_img = resize_image(product_img, (config.IMAGE_SIZE, config.IMAGE_SIZE))
    except FileNotFoundError:
        print(f"Error: Product image '{product_image}' not found. Skipping.")
        return

    # Generate images for each background prompt
    for prompt in background_prompts:
        combined_prompt = combine_product_and_background_prompt(product_image, prompt)
        try:
            generated_image = generator.generate_image(combined_prompt)
            output_filename = f"{product_image}_with_{prompt}.jpg"
            save_image(generated_image, os.path.join(config.OUTPUT_DIR, output_filename))
            print(f"Generated image: {output_filename}")
        except Exception as e:
            print(f"Error generating image with prompt '{prompt}': {e}")

if __name__ == "__main__":
    # Load product image list and background prompts (replace with your data)
    product_images = ["product1.jpg", "product2.png"]
    background_prompts = ["a modern living room with a couch", "a sunny beach with clear water"]

    # Generate images for each product
    for product_image in product_images:
        generate_ad_image(product_image, background_prompts)
