import unittest
from netmon.alerts.alerting_system import send_alert

class TestAlertingSystem(unittest.TestCase):

    def test_send_alert(self):
        result = send_alert('test@example.com', 'Test Subject', 'Test Message', smtp_server='smtp.test.com', smtp_user='user@test.com', smtp_password='password')
        self.assertIsInstance(result, bool)

if __name__ == '__main__':
    unittest.main()

