#import unitest as unittest
import unittest
import controlModule

#a unitest that asserts that the controlModule.py file is working correctly
class TestControlModule(unittest.TestCase):
    def test_controlModule(self):
        self.assertIsNotNone(controlModule.Trajectory(1,2,3,4),"null trajectory")



#cli command to run the unitest
#python -m unittest controlModuleTest