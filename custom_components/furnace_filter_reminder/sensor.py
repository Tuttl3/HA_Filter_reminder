from homeassistant.helpers.entity import Entity

class FurnaceFilterSensor(Entity):
    def __init__(self, name, hours):
        self._name = name
        self._threshold_hours = hours
        self._runtime = 0

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return max(0, self._threshold_hours - self._runtime)

    @property
    def extra_state_attributes(self):
        return {
            "runtime_hours": self._runtime,
            "threshold_hours": self._threshold_hours,
        }

    def increment_runtime(self, hours):
        self._runtime += hours

    def reset_runtime(self):
        self._runtime = 0
