import unittest
from netmon.monitors.latency_measure import measure_latency

class TestLatencyMeasure(unittest.TestCase):

    def test_measure_latency(self):
        result = measure_latency('127.0.0.1')
        self.assertIsInstance(result, float)

if __name__ == '__main__':
    unittest.main()

