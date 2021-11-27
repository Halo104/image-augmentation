from PIL import Image
import random


def random_augmentation(image: Image):
    augmentations = [rotate, fliplr, do_nothing, zoom]
    func = random.choice(augmentations)
    return func(image)


def do_nothing(image: Image):
    return image


def fliplr(image: Image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def rotate(image: Image):
    return image.rotate(random.randint(0, 365))


def zoom(image: Image):
    return image.transform(image.size, Image.EXTENT, data=(0, 1, image.width // 1.5, image.height // 1.5))
