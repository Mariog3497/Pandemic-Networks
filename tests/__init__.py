import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

from . import test_main, test_network  

suite.addTests(loader.loadTestsFromModule(test_main))
suite.addTests(loader.loadTestsFromModule(test_network))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)