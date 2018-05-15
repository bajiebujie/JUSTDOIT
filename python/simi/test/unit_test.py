#! encoding: utf8
import unittest


class UnitTest(unittest.TestCase):
    def setUp(self):
        print 'setUp'
        pass

    def tearDown(self):
        print 'tearDown'
        pass

    def test_sth(self):
        self.assertEquals(1, 1)


if __name__ == '__main__':
    unittest.main()
