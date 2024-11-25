from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_HOURS
from homeassistant.core import HomeAssistant
import datetime

DOMAIN = "furnace_filter_reminder"

class FurnaceFilterSensor(SensorEntity):
    def __init__(self, hass: HomeAssistant, config):
        self.hass = hass
        self.name = config.get("name", "Furnace Filter Runtime")
        self.threshold_hours = config.get(CONF_HOURS, 300)
        self.runtime = 0
        self.last_reset = datetime.datetime.now()

    @property
    def state(self):
        return max(0, self.threshold_hours - self.runtime)

    @property
    def extra_state_attributes(self):
        return {
            "runtime_hours": self.runtime,
            "threshold_hours": self.threshold_hours,
            "last_reset": self.last_reset,
        }

    def increment_runtime(self, hours):
        self.runtime += hours
        self.hass.states.set(self.entity_id, self.state)

    def reset_runtime(self):
        self.runtime = 0
        self.last_reset = datetime.datetime.now()
