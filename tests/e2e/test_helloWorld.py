import unittest
from .util.TestUtil import popenProcessBoss, getFixturePath, getFixturesDirPath

class TestHelloWorld(unittest.TestCase):

    def testHelloWorld(self):
        p, output = popenProcessBoss( getFixturePath("config_helloWorld.yaml"), getFixturesDirPath() )
        
        self.assertRegex(output, r"Hello World!", f"ACTUAL OUTPUT: {output}")
        self.assertEqual(p.returncode, 0)

if __name__ == '__main__':
    unittest.main()
