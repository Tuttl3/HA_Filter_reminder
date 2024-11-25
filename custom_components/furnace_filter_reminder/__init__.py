from homeassistant.core import HomeAssistant

DOMAIN = "furnace_filter_reminder"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration using YAML."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up the integration from the UI."""
    hass.data[DOMAIN] = entry.data
    return True
