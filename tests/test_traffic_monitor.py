import unittest
from netmon.monitors.bandwidth_analysis import bandwidth_analysis

class TestTrafficMonitor(unittest.TestCase):

    def test_bandwidth_analysis(self):
        result = bandwidth_analysis(1)
        self.assertIsInstance(result, dict)
        self.assertIn('bytes_sent', result)
        self.assertIn('bytes_recv', result)
        self.assertIn('interval', result)
        self.assertIsInstance(result['bytes_sent'], int)
        self.assertIsInstance(result['bytes_recv'], int)
        self.assertIsInstance(result['interval'], int)

if __name__ == '__main__':
    unittest.main()

