from PIL import Image

def resize_image(image, size):
    """Resizes an image to the specified size.

    Args:
        image (PIL.Image): Image to resize.
        size (tuple): Target size (width, height).

    Returns:
        PIL.Image: Resized image.
    """
    return image.resize(size)

def save_image(image, filename):
    """Saves an image to a file.

    Args:
        image (PIL.Image): Image to save.
        filename (str): Output filename.
    """
    image.save(filename)

def composite_images(background, product, position=(0, 0)):
    """Composites a product image onto a background image.

    Args:
        background (PIL.Image): Background image.
        product (PIL.Image): Product image.
        position (tuple): Position to place the product on the background.

    Returns:
        PIL.Image: Composited image.
    """
    background.paste(product, position, product)
    return background