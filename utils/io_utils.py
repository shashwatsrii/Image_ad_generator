import os

def create_output_directory(directory):
    """Creates the output directory if it doesn't exist.

    Args:
        directory (str): Path to the directory.

    Returns:
        None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_image_paths(directory):
    """Gets all image paths from the specified directory.

    Args:
        directory (str): Path to the directory.

    Returns:
        list: List of image paths.
    """
    return [os.path.join(directory, fname) for fname in os.listdir(directory) if fname.endswith(('.png', '.jpg', '.jpeg'))]
