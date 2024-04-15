"""This module defines the SideCondition class, which represents a in-battle side
condition.
"""
import logging
from enum import Enum, auto, unique


@unique
class SideCondition(Enum):
    """Enumeration, represent a in-battle side condition."""

    UNKNOWN = auto()
    AURORA_VEIL = auto()
    FIRE_PLEDGE = auto()
    G_MAX_CANNONADE = auto()
    G_MAX_STEELSURGE = auto()
    G_MAX_VINE_LASH = auto()
    G_MAX_VOLCALITH = auto()
    G_MAX_WILDFIRE = auto()
    GRASS_PLEDGE = auto()
    LIGHT_SCREEN = auto()
    LUCKY_CHANT = auto()
    MIST = auto()
    REFLECT = auto()
    SAFEGUARD = auto()
    SPIKES = auto()
    STEALTH_ROCK = auto()
    STICKY_WEB = auto()
    TAILWIND = auto()
    TOXIC_SPIKES = auto()
    WATER_PLEDGE = auto()

    def __str__(self) -> str:
        return f"{self.name} (side condition) object"

    @staticmethod
    def from_showdown_message(message: str):
        """Returns the SideCondition object corresponding to the message.

        :param message: The message to convert.
        :type message: str
        :return: The corresponding SideCondition object.
        :rtype: SideCondition
        """
        condition = message.replace("move: ", "").replace(" ", "_").replace("-", "_").upper()

        try:
            return SideCondition[condition]
        except KeyError:
            # try to catch messages w/o spacing
            for known_condition in SideCondition:
                if known_condition.name.replace("_", "") == condition:
                    return known_condition
            logging.getLogger("poke-env").warning(
                "Unexpected side condition '%s' received. SideCondition.UNKNOWN will be"
                " used instead. If this is unexpected, please open an issue at "
                "https://github.com/hsahovic/poke-env/issues/ along with this error "
                "message and a description of your program.",
                message,
            )
            return SideCondition.UNKNOWN


# SideCondition -> Max useful stack level
STACKABLE_CONDITIONS = {SideCondition.SPIKES: 3, SideCondition.TOXIC_SPIKES: 2}
