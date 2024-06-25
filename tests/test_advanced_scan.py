import unittest
from netmon.scanners.advanced_scan import advanced_scan

class TestAdvancedScan(unittest.TestCase):

    def test_advanced_scan(self):
        result = advanced_scan('127.0.0.1')
        self.assertIsInstance(result, dict)
        self.assertIn('hostname', result)
        self.assertIn('os', result)
        self.assertIn('open_ports', result)
        self.assertIsInstance(result['open_ports'], list)
        if result['open_ports']:
            self.assertTrue(all(isinstance(port_info, dict) for port_info in result['open_ports']))
            self.assertTrue(all('port' in port_info for port_info in result['open_ports']))
            self.assertTrue(all('service' in port_info for port_info in result['open_ports']))
            self.assertTrue(all('version' in port_info for port_info in result['open_ports']))
            self.assertTrue(all('product' in port_info for port_info in result['open_ports']))

if __name__ == '__main__':
    unittest.main()

