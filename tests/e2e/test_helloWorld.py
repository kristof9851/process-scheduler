import unittest
from .util.TestUtil import popenProcessBoss, getFixturePath, getFixturesDirPath

class TestHelloWorld(unittest.TestCase):

    def testHelloWorld(self):
        p, output = popenProcessBoss( getFixturePath("config_helloWorld.yaml"), getFixturesDirPath() )
        
        self.assertEqual(p.returncode, 0)
        self.assertTrue("Hello World!" in output)

if __name__ == '__main__':
    unittest.main()
