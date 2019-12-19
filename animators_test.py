import unittest
from animators import Animator

class TestAnimator(unittest.TestCase):

    def test_number(self):
        a = Animator(0, 0, 4, 4)

        self.assertEqual(a.value(0), 0, 'Should be 0')
        self.assertEqual(a.value(1), 1, 'Should be 1')
        self.assertEqual(a.value(2), 2, 'Should be 2')
        self.assertEqual(a.value(3), 3, 'Should be 3')
        self.assertEqual(a.value(4), 4, 'Should be 4')
        self.assertTrue(a.done, 'Should be done when animation complete')

    def test_list(self):
        a = Animator(0, [0, 0, 4], [4, 10, 0], 4)

        self.assertEqual(a.value(0), [0, 0, 4], 'Should be [0, 0, 4]')
        self.assertEqual(a.value(1), [1, 2.5, 3], 'Should be [1, 2.5, 3]')
        self.assertEqual(a.value(2), [2, 5, 2], 'Should be [2, 5, 2]')
        self.assertEqual(a.value(3), [3, 7.5, 1], 'Should be [3, 7.5, 1]')
        self.assertEqual(a.value(4), [4, 10, 0], 'Should be [4, 10, 0]')
        self.assertTrue(a.done, 'Should be done when animation complete')

if __name__ == '__main__':
    unittest.main()