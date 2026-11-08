"""Constants for config."""

from typing import TYPE_CHECKING

from homeassistant.util.hass_dict import HassKey

if TYPE_CHECKING:
    from .automation import EditAutomationConfigView

ACTION_CREATE_UPDATE = "create_update"
ACTION_DELETE = "delete"
DOMAIN = "config"
LLM_API_AUTOMATION_EDITING = "automation_editing"

DATA_AUTOMATION_CONFIG_VIEW: HassKey[EditAutomationConfigView] = HassKey(
    f"{DOMAIN}_automation_config_view"
)
