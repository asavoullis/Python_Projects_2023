"""Simple Captcha Generator

This script generates a simple captcha image using Python and PIL (Python Imaging Library).
The captcha text is a random combination of letters and digits.

Prerequisites:
- Make sure you have Python installed on your system.
- Install the required dependencies by running: `pip install -r requirements.txt`

Usage:
- Run the `captcha_generator.py` script to generate a captcha image.
- Customize the captcha size, characters, and length in the `captcha_generator.py` script.
"""

from PIL import Image, ImageDraw, ImageFont
import random
import string

def generate_captcha(size=(200, 100), characters=string.ascii_letters + string.digits, length=6):
    """Generate a captcha image.

    Args:
    - size (tuple): The size of the captcha image (width, height).
    - characters (str): The characters to use for captcha text.
    - length (int): The length of the captcha text.

    Returns:
    None
    """
    # Create a new image with a white background
    image = Image.new('RGB', size, 'white')
    draw = ImageDraw.Draw(image)

    # Choose a font (you need to have a font file, e.g., 'arial.ttf' in the current directory)
    try:
        font = ImageFont.truetype('arial.ttf', 36)
    except IOError:
        font = ImageFont.load_default()

    # Generate a random string for the captcha
    captcha_text = ''.join(random.choice(characters) for _ in range(length))

    # Draw the text on the image
    text_width, text_height = draw.textsize(captcha_text, font)
    x = (size[0] - text_width) / 2
    y = (size[1] - text_height) / 2
    draw.text((x, y), captcha_text, font=font, fill='black')

    # Save or display the captcha image
    image.save('captcha.png')
    image.show()

if __name__ == "__main__":
    generate_captcha()
