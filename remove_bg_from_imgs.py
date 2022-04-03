from PIL import Image, ImageChops
import os

os.system("pip3 install rembg")


def delete_images(input_file: str):
    os.system(f'rm -f {input_file}')


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


def rem_bg(input_file: str):
    input_file_list = input_file.split("/")
    act_dir = input_file_list[:-1]
    processed_dir = "/".join(act_dir) + "/processed_imgs/"

    # Check wether result dir exists and create it if it doesnt
    if not os.path.isdir(processed_dir):
        os.mkdir(processed_dir)

    file_name = input_file_list[-1].split(".")[0]
    output_file = processed_dir + file_name + ".png"

    comando = f'rembg i {input_file} {output_file}'
    os.system(comando)

    im = Image.open(output_file)
    im = trim(im)

    os.system(f'rm -f {output_file}')
    im.save(output_file)

    print(output_file)
