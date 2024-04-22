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
