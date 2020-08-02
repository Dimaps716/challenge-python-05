import math


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = pow(2, side)
    return area
    


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = base * height
    return area
    


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = (base * height) / 2
    return area
    


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = (diagonal_1 * diagonal_2) / 2
    return area
    


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = height * ((base_minor + base_major)/ 2)
    return area


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    area = (perimeter * apothem) / 2
    return area
    


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    area = round((math.pi * pow(radius, 2)) / 2)
    return area
    


if __name__ == '__main__':
    import unittest
    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initi8alize the needed values for the tests
            self.values = {
                'square_area': 16,
                'rectangle_area' : 40,
                'triangle_area' : 9,
                'rhombus_area' : 12,
                'trapezoid_area' : 56.0,
                'regular_polygon_area' : 9,
                'circumference_area' : 6
            }

        def test_square_area(self):
        # Make this test first...
            value = self.values.get('square_area')
            self.assertEqual(value, square_area(4))


        def test_rectangle_area(self):
        # Make this test first...
            value = self.values.get('rectangle_area')
            self.assertEqual(value, rectangle_area(8, 5))


        def test_triangle_area(self):
        # Make this test first...
            value = self.values.get('triangle_area')
            self.assertEqual(value, triangle_area(6, 3))

        def test_rhombus_area(self):
        # Make this test first...
            value = self.values.get('rhombus_area')
            self.assertEqual(value, rhombus_area(6, 4))

        def test_trapezoid_area(self):
        # Make this test first...
            value = self.values.get('trapezoid_area')
            self.assertEqual(value, trapezoid_area(8, 8, 7))
    

        def test_regular_polygon_area(self):
        # Make this test first...
            value = self.values.get('regular_polygon_area')
            self.assertEqual(value, regular_polygon_area(6, 3))

        def test_circumference_area(self):
        # Make this test first...
            value = self.values.get('circumference_area')
            self.assertEqual(value, circumference_area(2))


        def tearDown(self):
        # Delete the needed values for the tests
            del(self.values)
            

    unittest.main()
