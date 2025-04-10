from rembg import new_session, remove
from PIL import Image

input_path = 'dog.jpg'
output_path = 'dog-.png'
session = new_session("u2net-anime")
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        Input = i.read()
        Output = remove(Input, session=session)
        o.write(Output)

def remove_white_background(image_path):
    image = Image.open(image_path).convert('RGBA')
    pixels = image.load()
    
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if pixels[x, y] == (255, 255, 255, 255):
                pixels[x, y] = (255, 255, 255, 0)
    return image

output_path_white = 'dog-white.png'
image = remove_white_background(output_path)
image.save(output_path_white)