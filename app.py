import os
import click
from PIL import Image
import pillow_avif


@click.command()
@click.option('--format', '-f', default='webp', help='Select the format to convert avif or webp. Default value webp')
@click.option('--size', '-s', default=750, help='Select a width for images example 500. Deafult value 750')
@click.option('--compress', '-c', default=70, help='Select compress level example 80. Default value 70')
@click.option('--delete', '-d', default=0, help='Delete all original files 1 for delete original files. Defaul value 0')


def convertResize(format, size, compress, delete):

    folder = 'images/'
    extensions = ['.jpg', '.jpeg', '.png', '.webp', '.avif']

    for root, dirs, files in os.walk(folder):

        for file in files:

            # Convert file
                
                if any(file.lower().endswith(ext) for ext in extensions):
                    file = os.path.join(root, file)

                    name, file = os.path.splitext(file)
                    newFile = file.replace(file, f".{format}")
                    imgPath = name+file
                    nameFile = name.replace("images/", '')

                    print(f"[WORKING ON]: {imgPath}")
                 
                    try:
                        
                        im = Image.open(imgPath).convert('RGB')
                        im.save(name+newFile, str(format))

                    except:
                        print(f"This file {nameFile+newFile} could not be converted.")


                    # Resize and compress file
                    pathFile = name+newFile
                    image = Image.open(pathFile)

                    width, height = image.size
                    newWidth = size

                    try:
                        if size != 0:
                            newHeight = int(height * (newWidth / width))
                            resizedImg = im.resize( (newWidth, newHeight), resample=Image.LANCZOS )
                            resizedImg.save(pathFile, optimize=True, quality= compress)
                        
                        if size == 0:
                            im.save(pathFile, optimize=True, quality= compress)

                
                        print(f"[DONE]: {pathFile}")
                        
                    except:
                        print(f"[ERROR MESSAGES]: Resize fail !")

                    try:
                        if delete == 1:
                            os.remove(imgPath)
                            print(f"[MESSAGES]: Done !")
                    except:
                        pass

    exec(open('notify.py').read())

if __name__ == '__main__':
    convertResize()
    
