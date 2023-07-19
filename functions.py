from transformers import BlipProcessor, BlipForConditionalGeneration
import unittest
from PIL import Image
from loguru import logger


def get_image_caption(image_path):
    image = Image.open(image_path).convert('RGB')

    model_name= 'Salesforce/blip-image-captioning-large'
    device = 'cpu'

    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)

    inputs = processor(image, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_new_tokens=20)

    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

if __name__ == '__main__':
    image_path = r'C:\Users\S9053161\Documents\projects\yolo\train-yolov8-custom-dataset-step-by-step-guide\local_env\data\images\test\0b2a2c061ef16759.jpg'
    class ImageTest(unittest.TestCase):
        def test_get_image_caption(self):
            caption = get_image_caption(image_path)
            logger.info(caption)

    RUN_ALL = False
    if RUN_ALL:
        unittest.main()
    else:
        suite = unittest.TestSuite()
        suite.addTest(ImageTest('test_get_image_caption'))
        runner = unittest.TextTestRunner()
        runner.run(suite)