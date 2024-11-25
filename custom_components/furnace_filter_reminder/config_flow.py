import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_HOURS

DOMAIN = "furnace_filter_reminder"

class FurnaceFilterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        pass

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_NAME, default="Furnace Filter Reminder"): str,
            vol.Required(CONF_HOURS, default=300): int,
        })

        return self.async_show_form(step_id="user", data_schema=schema)
