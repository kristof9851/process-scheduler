import unittest
import logging
from process_boss.domain.config.processes.Process import Process
from unittest.mock import MagicMock

class TestProcess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.error = MagicMock()

    def testInitValidConfig(self):
        config = {
            "id": "my_process",
            "cron": "* * * * *",
            "command": "echo hello world",
            "runAtStartup": True
        }
        process = Process(config)

        self.assertEqual(process.id, config["id"])
        self.assertEqual(process.cron, config["cron"])
        self.assertEqual(process.command, config["command"])
        self.assertEqual(process.runAtStartup, config["runAtStartup"])

    def testInitMissingId(self):
        config = {
            "cron": "* * * * *",
            "command": "echo hello world",
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'^Invalid configuration for "id": Non-empty string required')

    def testInitInvalidIdType(self):
        config = {
            "id": 123,
            "cron": "* * * * *",
            "command": "echo hello world",
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'^Invalid configuration for "id": Non-empty string required')

    def testInitEmptyId(self):
        config = {
            "id": "",
            "cron": "* * * * *",
            "command": "echo hello world",
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'^Invalid configuration for "id": Non-empty string required')

    def testInitMissingCron(self):
        config = {
            "id": "my_process",
            "command": "echo hello world",
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'Invalid configuration for "cron": Non-empty string required')

    def testInitInvalidCronType(self):
        config = {
            "id": "my_process",
            "cron": 123,
            "command": "echo hello world",
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'Invalid configuration for "cron": Non-empty string required')

    def testInitEmptyCron(self):
        config = {
            "id": "my_process",
            "cron": "",
            "command": "echo hello world",
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'nvalid configuration for "cron": Non-empty string required')

    def testInitMissingCommand(self):
        config = {
            "id": "my_process",
            "cron": "* * * * *",
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'Invalid configuration for "command": Non-empty string required')

    def testInitInvalidCommandType(self):
        config = {
            "id": "my_process",
            "cron": "* * * * *",
            "command": 123,
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'Invalid configuration for "command": Non-empty string required')
    
    def testInitEmptyCommand(self):
        config = {
            "id": "my_process",
            "cron": "* * * * *",
            "runAtStartup": True
        }
        with self.assertRaises(Exception) as context:
            Process(config)
        self.assertRegex(str(context.exception), r'Invalid configuration for "command": Non-empty string required')

if __name__ == '__main__':
    unittest.main()
