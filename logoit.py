
import os
from PIL import Image

LOGO_FILENAME = 'example_logo.png'
LOGO_WIDTH = 80
LOGO_HEIGHT = 80
LOGO_DIR = 'withLogo'

logo = Image.open(LOGO_FILENAME)
logo = logo.resize((LOGO_WIDTH,LOGO_HEIGHT))

os.makedirs(LOGO_DIR, exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg')) or filename == LOGO_FILENAME:
        continue
        
    im = Image.open(filename)
    im_width, im_height = im.size

    # Add logo
    print('Adding logo to %s...' % filename)
    im.paste(logo, (im_width - LOGO_WIDTH, im_height - LOGO_HEIGHT), logo)

    # Save image
    im.save(os.path.join(LOGO_DIR, filename))
