```plaintext
image_ad_generator/
├── config.py                    # Configuration file for paths, model parameters
├── data/
│   ├── input_product/           # Folder for product images (white background)
│   └── background_images/       # Folder for optional pre-defined backgrounds (optional)
├── models/
│   └── stable_diffusion.py      # Stable Diffusion model wrapper
├── utils/
│   ├── image_utils.py           # Image processing utilities
│   └── prompt_utils.py          # Prompt generation utilities
└── main.py                      # Main script for processing and generation
