from rembg import remove
from PIL import Image
import io
import glob

files = glob.glob("images/*.png")
len(files)

for file in files:
    input_path = file
    output_path = input_path.replace("images", "results")

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            original_image = i.read()
            output = remove(original_image)
            o.write(output)
