import unittest
from netmon.scanners.port_scan import port_scan

class TestPortScan(unittest.TestCase):

    def test_port_scan(self):
        result = port_scan('127.0.0.1', range(20, 25))
        self.assertIsInstance(result, list)
        if result:
            self.assertTrue(all(isinstance(port_info, dict) for port_info in result))
            self.assertTrue(all('port' in port_info for port_info in result))
            self.assertTrue(all('service' in port_info for port_info in result))
            self.assertTrue(all('version' in port_info for port_info in result))
            self.assertTrue(all('product' in port_info for port_info in result))

if __name__ == '__main__':
    unittest.main()

