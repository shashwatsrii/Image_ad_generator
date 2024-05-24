from diffusers import StableDiffusionPipeline
from config import NUM_INFERENCE_STEPS

class StableDiffusionGenerator:
    def __init__(self, model_name):
        self.pipe = StableDiffusionPipeline.from_pretrained(model_name)

    def generate_image(self, prompt, num_inference_steps=NUM_INFERENCE_STEPS):
        """Generates an image using Stable Diffusion.

        Args:
            prompt (str): Text prompt describing the desired image.
            num_inference_steps (int): Number of inference steps (iterations).

        Returns:
            PIL.Image: Generated image.
        """
        image = self.pipe(prompt, num_inference_steps=num_inference_steps)["images"][0]
        return image
