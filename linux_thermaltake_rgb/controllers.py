"""
linux_thermaltake_rgb
Software to control your thermaltake hardware
Copyright (C) 2018  Max Chesterfield (chestm007@hotmail.com)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
from linux_thermaltake_rgb import drivers, LOGGER
from linux_thermaltake_rgb.classified_object import ClassifiedObject


class ThermaltakeController(ClassifiedObject):
    def __init__(self):
        self.devices = {}
        self.driver = None

    @classmethod
    def factory(cls, unit_type, unit_identifier=None):
        subclass_dict = {clazz.model: clazz for clazz in cls.inheritors()}
        try:
            # TODO: remove copy pasta
            if unit_identifier is not None:
                return subclass_dict.get(unit_type.lower())(unit=unit_identifier)
            else:
                return subclass_dict.get(unit_type.lower())()
        except KeyError as e:
            LOGGER.warn('%s not a valid controller type', e)

    def attach_device(self, port=None, dev=None):
        self.devices[port] = dev
        return self.devices[port]

    def save_profile(self):
        self.driver.save_profile()


class ThermaltakeG3Controller(ThermaltakeController):
    model = 'g3'

    def __init__(self, unit=1):
        super().__init__()
        self.unit = unit
        self.ports = 5
        self.driver = drivers.ThermaltakeG3ControllerDriver(unit)

