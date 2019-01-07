import os

import yaml
from mock import patch

from base_test_object import BaseTestObject
from linux_thermaltake_rgb.controllers import ThermaltakeController
from linux_thermaltake_rgb.daemon.config import Config
from linux_thermaltake_rgb.devices import ThermaltakeDevice
from linux_thermaltake_rgb.devices.psus import ThermaltakePSUDevice


class ConfigTest(BaseTestObject):
    @patch('linux_thermaltake_rgb.drivers.ThermaltakeControllerDriver._initialize_device', autospec=True)
    def test_load_from_assets(self, init_dev):
        def verify_config(config):
            for thing in (config, config.controllers, config.fan_manager, config.lighting_manager):
                self.assertIsNotNone(thing)

        # verify absolute load codepath is good
        Config.abs_config_dir = str(Config.rel_config_dir)
        verify_config(Config())

        # verify relative load codepath is good
        Config.rel_config_dir = Config.abs_config_dir
        del Config.abs_config_dir
        Config.abs_config_dir = ''
        verify_config(Config())

    @patch('linux_thermaltake_rgb.drivers.ThermaltakeControllerDriver._initialize_device', autospec=True)
    def test_g3_config(self, init_dev):
        class MockConfig(Config):
            def load_config(self):
                return yaml.load(G3_CONFIG)
        config = MockConfig()
        self.assertEqual(len(config.controllers), 5, 'not all controllers recognized in config')
        for controller in config.controllers:
            self.assertEqual(controller.get('type'), 'g3')
            self.assertIn('unit', controller)

            ThermaltakeController.factory(controller.get('type'))
            self.assertTrue(init_dev.called)

    @patch('linux_thermaltake_rgb.drivers.ThermaltakeControllerDriver._initialize_device', autospec=True)
    def test_irgbplus_config(self, init_dev):
        class MockConfig(Config):
            def load_config(self):
                return yaml.load(IRGBPLUS_CONFIG)

        config = MockConfig()
        for psu in config.psus:
            self.assertEqual(psu.get('type'), 'irgbplus')

            dev = ThermaltakeDevice.factory(psu.get('type'))
            self.assertIsInstance(dev, ThermaltakePSUDevice)
            self.assertTrue(init_dev.called)


IRGBPLUS_CONFIG = """
psus:
  - type: irgbplus
"""

G3_CONFIG = """
controllers:
  - unit: 1
    type: g3
    devices:
      1: Riing Plus
      2: Riing Plus
      3: Riing Plus
      4: Riing Plus
      5: Floe Riing RGB
  - unit: 2
    type: g3
    devices:
      1: Riing Plus
      2: Riing Plus
      3: Riing Plus
      4: Pacific V-GTX 1080Ti Plus GPU Waterblock
      5: Pacific W4 Plus CPU Waterblock
  - unit: 3
    type: g3
    devices:
      1: Riing Plus
      2: Riing Plus
      3: Riing Plus
      4: Pacific V-GTX 1080Ti Plus GPU Waterblock
      5: Pacific PR22-D5 Plus
  - unit: 4
    type: g3
    devices:
      1: Riing Plus
      2: Riing Plus
      3: Riing Plus
      4: Pacific V-GTX 1080Ti Plus GPU Waterblock
      5: Lumi Plus LED Strip
  - unit: 5
    type: g3
    devices:
      1: Riing Plus
      2: Riing Plus
      3: Riing Plus
      4: Riing Plus
      5: Lumi Plus LED Strip
"""
