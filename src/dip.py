from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass


class Light(Device):
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class Fan(Device):
    def turn_on(self):
        print("Fan is spinning")

    def turn_off(self):
        print("Fan is stopped")


class Button:
    def __init__(self, device: Device):
        self._device = device

    def press(self):
        self._device.turn_on()


# Usage
light = Light()
fan = Fan()

light_button = Button(light)
fan_button = Button(fan)

light_button.press()
fan_button.press()