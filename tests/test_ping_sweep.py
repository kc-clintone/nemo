import unittest
from network_tool.scanners.ping_sweep import ping_sweep

class TestPingSweep(unittest.TestCase):

    def test_ping_sweep(self):
        hosts = ping_sweep("192.168.1.1/24")
        self.assertIsInstance(hosts, list)

if __name__ == '__main__':
    unittest.main()

