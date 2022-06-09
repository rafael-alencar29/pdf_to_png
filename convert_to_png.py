import os
from os import path
from glob import glob
from pdf2image import convert_from_path
from pathlib import Path


def find_ext(directory, ext):
    return glob(path.join(directory, "*.{}".format(ext)))


def convert_pdf_to_img(parent_dir, directories):

    new_files = []

    for file in directories:
        images = []
        file_name = os.path.basename(file)
        new_file = os.path.splitext(file_name)[0]
        new_files.append(new_file)

        path = os.path.join(parent_dir, new_file)
        os.mkdir(path)

        images = convert_from_path(file_name)

        for i in range(len(images)):
            # Save pages as images 
            name = "page"+str(i+1)+".png"
            save_path = os.path.join(path, name)
            #images[i].save(path, 'page' + str(i+1) + '.png', 'PNG')
            images[i].save(save_path, 'PNG')

    return new_files


# get current working directory
directory = os.getcwd()
print(directory)

directories = find_ext(directory, "pdf")


# create the new files where the imgs will be stored after conversion
print(directories)


file_imgs = convert_pdf_to_img(directory, directories)

for file in file_imgs:
    print("converted to img: ", file)

