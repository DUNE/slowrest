import pytest

from slowrest.utils import get_page_sensor_dict

def test_get_page_sensor_dict():
    assert isinstance(get_page_sensor_dict(), dict)
