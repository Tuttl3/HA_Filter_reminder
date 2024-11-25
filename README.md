
# Furnace Filter Reminder

A Home Assistant custom integration that tracks your furnace's runtime and reminds you to change the filter based on hours of operation. This integration works with compatible thermostats, such as Ecobee, connected via HomeKit.

## Features
- Tracks furnace runtime and calculates remaining hours until filter replacement.
- Lovelace dashboard card to display countdown and reset runtime.
- Configurable settings via UI:
  - Select your thermostat.
  - Set runtime threshold (e.g., 300 hours).
  - Choose notification methods (e.g., push notifications).
- Multiple reset options:
  - Button on the dashboard.
  - NFC trigger.
  - Physical sensor (optional).

---

## Installation

### Manual Installation
1. Download this repository as a `.zip` file or clone it:
   ```bash
   git clone https://github.com/Tuttl3/furnace_filter_reminder.git
   ```
2. Copy the `furnace_filter_reminder` folder into your Home Assistant `custom_components` directory. The path should look like this:
   ```
   config/custom_components/furnace_filter_reminder
   ```

3. Restart Home Assistant.

### Add to Lovelace Dashboard
1. Add the following Lovelace card (or install [Custom Button Card](https://github.com/custom-cards/button-card) for advanced visuals):
   ```yaml
   type: custom:button-card
   entity: sensor.furnace_filter_runtime
   name: Furnace Filter
   show_state: true
   tap_action:
     action: call-service
     service: furnace_filter_reminder.reset
     service_data:
       entity_id: sensor.furnace_filter_runtime
   ```

---

## Configuration

### Step 1: Add the Integration
1. Go to **Settings > Devices & Services** in Home Assistant.
2. Click **Add Integration** and search for "Furnace Filter Reminder."
3. Follow the setup wizard:
   - Select your thermostat.
   - Set runtime threshold (default is 300 hours).
   - Choose notification options.

### Step 2: Notifications (Optional)
If you want mobile notifications, ensure the `mobile_app` integration is enabled in Home Assistant. Replace `mobile_app_your_device` with your actual device ID in the automation (under `automation.py`).

---

## Usage

### Dashboard Countdown
- Displays the remaining runtime hours until a filter change is needed.
- Updates dynamically as the furnace runs.

### Reset Options
1. **Dashboard Button:** Tap the "Reset" button on the Lovelace card after changing the filter.
2. **NFC Tag:** Use Home Assistant’s NFC functionality to trigger the reset service:
   ```yaml
   - platform: tag
     tag_id: your_nfc_tag_id
     action:
       service: furnace_filter_reminder.reset
       data:
         entity_id: sensor.furnace_filter_runtime
   ```
3. **Physical Sensor (Optional):** Configure an external trigger, such as a button or switch, to reset the runtime.

---

## Advanced Customization

### Changing Runtime Threshold
1. Go to **Settings > Devices & Services.**
2. Find the Furnace Filter Reminder integration and click **Options.**
3. Adjust the runtime threshold and save.

### Adding Multiple Thermostats
To monitor multiple thermostats, set up a separate instance of the integration for each one.

---

## Troubleshooting

1. **Integration Not Found:**
   - Ensure the `furnace_filter_reminder` folder is in `custom_components` and restart Home Assistant.
2. **Notifications Not Working:**
   - Verify your notification service is correctly configured (e.g., `mobile_app` or `notify` services).

---

## Contributing

Contributions are welcome! If you encounter a bug or have a feature request:
1. Open an issue on the repository.
2. Submit a pull request with your changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
