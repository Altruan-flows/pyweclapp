"""This module provides functions for converting weclapp timestamps
to datetime objects and for converting datetime objects to various
string or integer representations."""

import datetime
from typing import Union
import zoneinfo


def convert_to_datetime(
    timestamp: Union[str, int, float], timezone: str = "Europe/Berlin"
) -> datetime.datetime:
    """Convert a weclapp timestamp to a datetime object in the specified timezone."""
    if not timestamp:
        raise ValueError("Timestamp must be provided as a non-empty string or number.")
    if isinstance(timestamp, str):
        try:
            float(timestamp)
        except ValueError:
            raise ValueError(
                f"Invalid time format: {timestamp}. Must be a numeric string or a number."
            )
    if not isinstance(timestamp, (int, float, str)):
        raise TypeError(
            f"Invalid type for timestamp: {type(timestamp)}. Must be int, float, or str."
        )
    try:
        timestamp = float(timestamp) / 1000
        relevant_time = datetime.datetime.fromtimestamp(
            timestamp, tz=zoneinfo.ZoneInfo(timezone)
        )

        return relevant_time
    except OverflowError as of:
        raise OverflowError(
            f"{of}, while converting {timestamp} to datetime object"
        ) from of


def convert_to_time_format(
    input_time: Union[datetime.date, datetime.datetime],
    conversion_format: str = "weclapp",
    timezone: str = "Europe/Berlin",
) -> Union[str, int]:
    """Converts a datetime object to a string or integer representation.
    Args:
        input_time (Union[datetime.date, datetime.datetime]): The
            time to convert. Can be a datetime object or date object.
        conversion_format (str): The format to convert the time to. Must be one of
            'unix', 'weclapp', 'emailDate', 'utcDate', or 'ads'.
            - 'unix': Returns the time as a Unix timestamp (int).
            - 'weclapp': Returns the time as a weclapp timestamp (int).
            - 'emailDate': Returns the time as an email date string (str).
            - 'utcDate': Returns the time as a UTC date string (str).
            - 'ads': Returns the time as an ADS date string (str).
    Returns:
        Union[str, int]: The converted time in the specified format.
    """
    try:
        if conversion_format == "unix":
            return int(input_time.timestamp())
        if conversion_format == "weclapp":
            return int(input_time.timestamp()) * 1000
        if conversion_format == "emailDate":
            return str(input_time.strftime("%d.%m.%Y"))
        if conversion_format == "utcDate":
            return str(input_time.strftime("%Y-%m-%d"))
        if conversion_format == "ads":
            # 2022-12-04 11:11:11-01:00
            aware_time = datetime.datetime(
                input_time.year,
                input_time.month,
                input_time.day,
                input_time.hour,
                input_time.minute,
                input_time.second,
                tzinfo=zoneinfo.ZoneInfo(timezone),
            )
            return aware_time.isoformat().replace("T", " ")

        raise ValueError(
            f"Invalid conversion format: {conversion_format}. Must be one of "
            "'unix', 'weclapp', 'emailDate', 'utcDate', or 'ads'."
        )

    except OverflowError as of:
        raise OverflowError(
            f"{of}, while transforming {input_time} to {conversion_format}"
        ) from of
