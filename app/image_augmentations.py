from PIL import Image
import random


def random_augmentation(image: Image) -> Image:
    #augmentations = [rotate, fliplr, do_nothing, zoom, greyscale]
    augmentations = [greyscale]
    func = random.choice(augmentations)
    return func(image)


def do_nothing(image: Image) -> Image:
    return image


def fliplr(image: Image) -> Image:
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def rotate(image: Image) -> Image:
    return image.rotate(random.randint(0, 365))


def zoom(image: Image) -> Image:
    zoomRatio = 1.5
    return image.transform(image.size, Image.EXTENT, data=(0, 1, image.width // zoomRatio, image.height // zoomRatio))


def greyscale(image: Image) -> Image:
    return image.convert('L')
