import unittest
import kNN_s

class TestkNN(unittest.TestCase):
    def test_classify0(self):
        group,labels = kNN_s.createDataSet()
        z=kNN_s.classify0([0,0],group,labels,3)
        self.assertEqual(z,'B')

if __name__ == '__main__':
    unittest.main()