from models.stable_diffusion import StableDiffusionGenerator
from utils.image_utils import resize_image, save_image, composite_images
from utils.prompt_utils import combine_product_and_background_prompt
from utils.io_utils import create_output_directory, get_image_paths
import config
from PIL import Image
import os

def generate_ad_image(product_image_path, background_prompts):
    """Generates advertisement images for a product with different backgrounds.

    Args:
        product_image_path (str): Path to the product image file.
        background_prompts (list): List of text prompts for different backgrounds.

    Returns:
        None
    """
    # Load Stable Diffusion model
    generator = StableDiffusionGenerator(config.MODEL_NAME)

    # Load and resize product image
    try:
        product_img = Image.open(product_image_path).convert("RGBA")
        product_img = resize_image(product_img, (config.IMAGE_SIZE, config.IMAGE_SIZE))
    except FileNotFoundError:
        print(f"Error: Product image '{product_image_path}' not found. Skipping.")
        return

    product_name = os.path.basename(product_image_path)
    create_output_directory(config.OUTPUT_DIR)

    # Generate images for each background prompt
    for prompt in background_prompts:
        combined_prompt = combine_product_and_background_prompt(product_name, prompt)
        try:
            generated_bg = generator.generate_image(combined_prompt)
            generated_bg = generated_bg.convert("RGBA")
            final_image = composite_images(generated_bg, product_img)
            output_filename = f"{product_name}_with_{prompt.replace(' ', '_')}.png"
            save_image(final_image, os.path.join(config.OUTPUT_DIR, output_filename))
            print(f"Generated image: {output_filename}")
        except Exception as e:
            print(f"Error generating image with prompt '{prompt}': {e}")

if __name__ == "__main__":
    product_images = get_image_paths(config.INPUT_PRODUCT_DIR)
    background_prompts = ["a modern living room", "a sunny beach with clear water"]

    for product_image in product_images:
        generate_ad_image(product_image, background_prompts)
