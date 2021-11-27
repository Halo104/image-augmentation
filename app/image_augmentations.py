from PIL import Image
import random


def random_augmentation(image: Image) -> Image:
    augmentations = [rotate, fliplr, do_nothing, greyscale]
    func = random.choice(augmentations)
    return func(image)


def do_nothing(image: Image) -> Image:
    return image


def fliplr(image: Image) -> Image:
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def rotate(image: Image) -> Image:
    return image.rotate(random.randint(0, 365))


def greyscale(image: Image) -> Image:
    return image.convert('L')
