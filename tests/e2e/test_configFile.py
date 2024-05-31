import unittest
from .util.TestUtil import popenProcessBoss, getFixturePath

class TestConfigFile(unittest.TestCase):

    def testMissingParameter(self):
        p, output = popenProcessBoss()
        
        self.assertEqual(p.returncode, 1)
        self.assertTrue("Missing CLI argument: Configuration File Path" in output)

    def testInvalidPath(self):
        p, output = popenProcessBoss("y:\\config.yaml")
        
        self.assertEqual(p.returncode, 1)
        self.assertTrue("Configuration file not found: \"y:\config.yaml\"" in output)

    def testEmptyFile(self):
        p, output = popenProcessBoss( getFixturePath("config_empty.yaml") )

        self.assertEqual(p.returncode, 1)
        self.assertTrue("You have to define at least one process!" in output)

if __name__ == '__main__':
    unittest.main()
