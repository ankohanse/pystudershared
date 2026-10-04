import pytest
import pytest_asyncio

from pystudershared import StuderDeviceFamilies, StuderDeviceFamily
from pystudershared import StuderDataset, StuderDatapoint, StuderDatapointUnknownException
from pystudershared import StuderUserLevel, StuderDataType, StuderAccess, StuderTarget
from pystudershared import StuderParamException


TEST_FAMILY_A = StuderDeviceFamily(id='aaa', model="model A")
TEST_FAMILY_B = StuderDeviceFamily(id='bbb', model="model B")
TEST_FAMILIES = StuderDeviceFamilies([TEST_FAMILY_A, TEST_FAMILY_B])

TEST_DATASET = StuderDataset(
    datapoints=[
        StuderDatapoint(family_id='aaa', parent_id='', id='a1', userlevel_r=StuderUserLevel.VIEWONLY, userlevel_w=StuderUserLevel.VIEWONLY, nr_or_addr=1, name='a1', label='A1', unit='', data_type=StuderDataType.INT32, size=2, access=StuderAccess.READ, target=StuderTarget.STANDARD, default=0, min=0, max=99, inc=1),
        StuderDatapoint(family_id='aaa', parent_id='', id='a2', userlevel_r=StuderUserLevel.VIEWONLY, userlevel_w=StuderUserLevel.VIEWONLY, nr_or_addr=2, name='a1', label='A1', unit='', data_type=StuderDataType.INT32, size=2, access=StuderAccess.READ, target=StuderTarget.STANDARD, default=0, min=0, max=99, inc=1),
        StuderDatapoint(family_id='aaa', parent_id='', id='a3', userlevel_r=StuderUserLevel.VIEWONLY, userlevel_w=StuderUserLevel.VIEWONLY, nr_or_addr=3, name='a1', label='A1', unit='', data_type=StuderDataType.INT32, size=2, access=StuderAccess.READ, target=StuderTarget.STANDARD, default=0, min=0, max=99, inc=1),
    ],
    families=TEST_FAMILIES
)


@pytest.mark.parametrize(
    "id, family, exp_id, exp_family_id, exp_except",
    [
        ("a2", TEST_FAMILY_A, 'a2', 'aaa', None),
        ("a2", 'aaa',         'a2', 'aaa', None),
        ("a2", None,          'a2', 'aaa', None),
        ("x1", TEST_FAMILY_A, None,  None, StuderDatapointUnknownException),
        ("x1", 'aaa',         None,  None, StuderDatapointUnknownException),
        ("x1", None,          None,  None, StuderDatapointUnknownException),
        (None, None,          None,  None, StuderParamException),
    ]
)
def test_get_by_id(id, family, exp_id, exp_family_id, exp_except):
    dataset = TEST_DATASET

    if not exp_except:
        dp = dataset.get_by_id(id, family)
        assert dp is not None
        assert dp.id == exp_id
        assert dp.family_id == exp_family_id
    else:
        with pytest.raises(exp_except):
            dp = dataset.get_by_id(id, family)


@pytest.mark.parametrize(
    "nr, family, exp_id, exp_family_id, exp_except",
    [
        (2,    TEST_FAMILY_A, 'a2', 'aaa', None),
        (2,    'aaa',         'a2', 'aaa', None),
        (99,   TEST_FAMILY_A, None,  None, StuderDatapointUnknownException),
        (99,   'aaa',         None,  None, StuderDatapointUnknownException),
        (None, 'aaa',         None,  None, StuderParamException),
        (2,    None,          None,  None, StuderParamException),
    ]
)
def test_get_by_nr(nr, family, exp_id, exp_family_id, exp_except):
    dataset = TEST_DATASET

    if not exp_except:
        dp = dataset.get_by_nr(nr, family)
        assert dp is not None
        assert dp.id == exp_id
        assert dp.family_id == exp_family_id
    else:
        with pytest.raises(exp_except):
            dp = dataset.get_by_nr(nr, family)


@pytest.mark.parametrize(
    "address, family, exp_id, exp_family_id, exp_except",
    [
        (2,    TEST_FAMILY_A, 'a2', 'aaa', None),
        (2,    'aaa',         'a2', 'aaa', None),
        (99,   TEST_FAMILY_A, None,  None, StuderDatapointUnknownException),
        (99,   'aaa',         None,  None, StuderDatapointUnknownException),
        (None, 'aaa',         None,  None, StuderParamException),
        (2,    None,          None,  None, StuderParamException),
    ]
)
def test_get_by_address(address, family, exp_id, exp_family_id, exp_except):
    dataset = TEST_DATASET

    if not exp_except:
        dp = dataset.get_by_address(address, family)
        assert dp is not None
        assert dp.id == exp_id
        assert dp.family_id == exp_family_id
    else:
        with pytest.raises(exp_except):
            dp = dataset.get_by_address(address, family)

