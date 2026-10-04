import pytest
import pytest_asyncio

from pystudershared import StuderDeviceFamilies, StuderDeviceFamily, StuderDeviceFamilyUnknownException


TEST_FAMILIES = StuderDeviceFamilies([
    StuderDeviceFamily(id='aaa', model="model A"),
    StuderDeviceFamily(id='bbb', model="model B"),
    StuderDeviceFamily(id='ccc', model="model C"),
    StuderDeviceFamily(id='ddd', model="model D"),
])


def test_id():
    families = TEST_FAMILIES
    for family in families:
        assert family == families.get_by_id(family.id)

    with pytest.raises(StuderDeviceFamilyUnknownException):
        family = families.get_by_id("XXX")
