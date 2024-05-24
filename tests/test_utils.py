import pytest
from PIL import Image
from utils.image_utils import resize_image, save_image, composite_images

def test_resize_image():
    img = Image.new('RGB', (100, 100))
    resized_img = resize_image(img, (50, 50))
    assert resized_img.size == (50, 50)

def test_save_image(tmp_path):
    img = Image.new('RGB', (100, 100))
    file_path = tmp_path / "test_image.jpg"
    save_image(img, file_path)
    assert file_path.exists()

def test_composite_images():
    bg = Image.new('RGBA', (100, 100), (255, 255, 255, 255))
    product = Image.new('RGBA', (50, 50), (0, 255, 0, 128))
    composited_img = composite_images(bg, product, position=(25, 25))
    assert composited_img.size == (100, 100)
    assert composited_img.getpixel((50, 50)) == (0, 255, 0, 128)
