import unittest
import task

class testdic(unittest.TestCase):
  D1=new_dic
  D2={'Mon': 2, 'Tue': 4.0, 'Wed': 6.0, 'Thu': 8.0, 'Fri': 10.0, 'Sat': 12.0, 'Sun': 14}
  def test(self):
        self.assertDictEqual(self.D1, self.D2)
if __name__ == '__main__':
    unittest.main()
