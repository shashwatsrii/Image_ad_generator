# Image Ad Generator

This project generates advertisement images by placing product images onto various background settings using Stable Diffusion.

IMAGE_AD_GENERATOR/
│
├── data/
│   ├── input_product/
│   │   ├── AmericanFootball.png
│   │   └── YellowCouch.png
│   └── background_images/
│       ├── living_room.jpg
│       └── beach.jpg
│   
├── env/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── share/
│
├── models/
│   └── stable_diffusion.py
│
├── output_images/
│   ├── AmericanFootball_with_a_modern_living_room.jpg
│   └── YellowCouch_with_a_sunny_beach_with_clear_water.jpg
│
├── tests/
│   └── test_image_utils.py
│
├── utils/
│   ├── image_utils.py
│   ├── prompt_utils.py
│   └── io_utils.py
│
├── config.py
├── main.py
├── requirements.txt
└── README.md

## Project Structure

- `data/`: Contains input product images and optional background images.
- `env/`: Virtual environment files.
- `models/`: Contains model-related code.
- `output_images/`: Directory where generated images are saved.
- `tests/`: Contains test cases for the project.
- `utils/`: Contains utility functions for image processing and prompt handling.
- `config.py`: Configuration file with model and path settings.
- `main.py`: Main script to run the image generation process.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## Setup

1. Clone the repository.
2. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
3. Run the main script:
    ```
    python main.py
    ```

## Usage

Place your product images in the `data/input_product/` directory. Modify the `background_prompts` list in `main.py` to add your own background descriptions.
