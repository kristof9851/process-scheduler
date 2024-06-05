import unittest
from .util.TestUtil import popenProcessBoss, getFixturePath

class TestConfigFile(unittest.TestCase):

    def testMissingParameter(self):
        p, output = popenProcessBoss()
        
        self.assertRegex(output, r"Missing CLI argument: Configuration File Path", f"ACTUAL OUTPUT: {output}")
        self.assertEqual(p.returncode, 1)

    def testInvalidPath(self):
        p, output = popenProcessBoss("non_existent_config.yaml")
        
        self.assertRegex(output, r"Configuration file not found: \"non_existent_config.yaml\"", f"ACTUAL OUTPUT: {output}")
        self.assertEqual(p.returncode, 1)

    def testEmptyFile(self):
        p, output = popenProcessBoss( getFixturePath("config_empty.yaml") )

        self.assertRegex(output, r"You have to define at least one process!", f"ACTUAL OUTPUT: {output}")
        self.assertEqual(p.returncode, 1)

if __name__ == '__main__':
    unittest.main()
