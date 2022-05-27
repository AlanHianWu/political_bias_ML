import unittest, time, sys, os

'''if file structure is right import dataprocessing here'''
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Data_Preprocessing import Preprocessing

class testDataPreprocessing(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(testDataPreprocessing, self).__init__(*args, **kwargs)

        self.preprocessing = Preprocessing()
    
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    '''test cases'''
    
    def test_remove_special(self):
        rm_sp = self.preprocessing.remove_special_characters('te$t')
        self.assertEqual(rm_sp, 'tet')

    
    def test_remove_special_threading(self):
        '''need to ensure testing for threading here'''
        rm_sp = self.preprocessing.remove_special_characters_multi('te$t')
        self.assertEqual(rm_sp, 'tet')

    



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testDataPreprocessing)
    unittest.TextTestRunner(verbosity=0).run(suite)