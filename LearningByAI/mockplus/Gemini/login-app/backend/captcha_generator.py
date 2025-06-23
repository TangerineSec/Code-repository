# backend/captcha_generator.py
from PIL import Image, ImageDraw, ImageFont
import random
import string

def get_random_color():
    """Generates a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_captcha_image(width=25, height=25, length=4):
    """
    Generates a captcha image with random text.
    """
    # Create a blank image with a light grey background
    image = Image.new('RGB', (width, height), (240, 240, 240))
    draw = ImageDraw.Draw(image)

    # Use a system font. You might need to provide a path to a .ttf file.
    # On Windows: 'arial.ttf'. On macOS/Linux, you might need to specify the full path.
    try:
        font = ImageFont.truetype('arial.ttf', size=24)
    except IOError:
        font = ImageFont.load_default()

    # Generate random text
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    # Draw the text on the image
    text_width, text_height = draw.textbbox((0, 0), captcha_text, font=font)[2:]
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), captcha_text, font=font, fill=get_random_color())
    # draw.text((text_x, text_y), captcha_text, font=font, fill=(0, 0, 0))

    # Add some noise (lines and pixels)
    for _ in range(3):
        draw.line([(random.randint(0, width), random.randint(0, height)),
                   (random.randint(0, width), random.randint(0, height))],
                  fill=get_random_color(), width=1)

    for _ in range(10):
        draw.point([(random.randint(0, width), random.randint(0, height))],
                   fill=get_random_color())

    return image, captcha_text
