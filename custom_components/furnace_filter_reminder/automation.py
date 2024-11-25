from homeassistant.helpers.event import async_track_state_change

async def async_setup(hass: HomeAssistant, config):
    sensor_entity = "sensor.furnace_filter_runtime"

    def check_runtime(entity, old_state, new_state):
        if int(new_state.state) <= 0:
            hass.services.call(
                "notify", "mobile_app_your_device", {"message": "Change your furnace filter!"}
            )

    async_track_state_change(hass, sensor_entity, check_runtime)
