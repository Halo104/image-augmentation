import unittest

from PIL import Image

from image_augmentations import greyscale


def create_test_image():
    test_image = Image.new('RGB', size=(100, 200), color=(200, 50, 50))
    return test_image


class ImageAugmentationsTest(unittest.TestCase):
    def test_greyscale_image_is_same_size(self):
        test_image = create_test_image()
        self.assertEqual(greyscale(test_image).width, 100, "Width should be 100")
        self.assertEqual(greyscale(test_image).height, 200, "Height should be 200")

    def test_greyscale_image_is_grey(self):
        test_image = greyscale(create_test_image())
        test_image = test_image.convert('RGB')
        width, height = test_image.size
        for w in range(width):
            for h in range(height):
                r, g, b = test_image.getpixel((w, h))
                self.assertEqual(r, g, "red and green should be same value")
                self.assertEqual(r, b, "red and blue should be same value")

        #Another method of testing for greyscale, by assuming only one colour band exists
        #self.assertEqual(len(test_image.getbands()), 1, "Should have only 1 band")


if __name__ == '__main__':
    # Run all the tests
    unittest.main()
