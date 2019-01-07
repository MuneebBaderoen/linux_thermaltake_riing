from mock import patch
from base_test_object import BaseTestObject
from linux_thermaltake_rgb.daemon.daemon import ThermaltakeDaemon, Config


class DaemonMockIntegrationTest(BaseTestObject):
    def setUp(self):
        self.config_abs_path = str(Config.abs_config_dir)
        Config.abs_config_dir = ''

    @patch('linux_thermaltake_rgb.drivers.ThermaltakeControllerDriver._initialize_device', autospec=True)
    def test_basic_startup(self, init_dev):
        daemon = ThermaltakeDaemon()
        self.assertIsNotNone(daemon)
        self.assertIsNotNone(daemon.config.controllers)
        self.assertTrue(init_dev.called)

    def tearDown(self):
        Config.abs_config_dir = str(self.config_abs_path)
