import unittest

#Practicing examples from my lessons.
class Rectangle:
    def __init__(rect, width, height):
        rect.width = width
        rect.height = height

    def get_area(rect):
        return rect.width * rect.height
    def set_width(rect, width):
        rect.width = width
    def set_height(rect, height):
        rect.height = height


class TestGetAreaRectangle(unittest.TestCase):
    def normal_test(rect):
        rectangle = Rectangle(2,3)
        rect.assertEqual(rectangle.get_area(), 6, "incorrect area")
    def test_geq(rect):
        rectangle = Rectangle(2,3)
        rect.assertGreaterEqual(rectangle.get_area(), -1)
unittest.main()