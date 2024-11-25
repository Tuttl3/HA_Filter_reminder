import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_NAME, CONF_HOURS

from .const import DOMAIN  # Create a `const.py` file with `DOMAIN = "furnace_filter_reminder"`

class FurnaceFilterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    @callback
    def async_get_options_flow(self, config_entry):
        return FurnaceFilterOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            # Save the configuration and create an entry
            return self.async_create_entry(
                title=user_input[CONF_NAME], data=user_input
            )

        # Show the form for user input
        data_schema = vol.Schema({
            vol.Required(CONF_NAME, default="Furnace Filter Reminder"): str,
            vol.Required(CONF_HOURS, default=300): int,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema)

class FurnaceFilterOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Optional(CONF_HOURS, default=self.config_entry.options.get(CONF_HOURS, 300)): int,
        })

        return self.async_show_form(step_id="init", data_schema=data_schema)
