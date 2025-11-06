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
    @classmethod
    def setUpClass(rect):
        rect.rectangle = Rectangle(0,0)
        
    def normal_test(rect):
        rect.rectangle.set_width(2)
        rect.rectangle.set_height(3)
        rect.assertEqual(rect.rectangle.get_area(), 6, "incorrect area")

    def test_geq(rect):
        rect.rectangle.set_width(22)
        rect.rectangle.set_height(33)
        rect.assertGreaterEqual(rect.rectangle.get_area(), -1)
    
    def test_assert_raises(rect):
        with rect.assertRaises(ZeroDivisionError):
            r = 1 / 0

unittest.main()