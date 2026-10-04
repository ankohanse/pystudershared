import pytest
import pytest_asyncio

from pystudershared import StuderDeviceFamilies, StuderDeviceFamily
from pystudershared import StuderDataset, StuderDatapoint, StuderDatapointUnknownException
from pystudershared import StuderUserLevel, StuderDataType, StuderAccess, StuderTarget
from pystudershared import StuderParamException


TEST_DATAPOINT_INT32    = StuderDatapoint(family_id='aaa', parent_id='', id='a1', userlevel_r=StuderUserLevel.VIEWONLY, userlevel_w=StuderUserLevel.VIEWONLY, nr_or_addr=1, name='a1', label='A1', unit='', data_type=StuderDataType.INT32,    size=2, access=StuderAccess.READ, target=StuderTarget.STANDARD, default=0, min=0, max=99, inc=1)
TEST_DATAPOINT_ENUM32   = StuderDatapoint(family_id='aaa', parent_id='', id='a2', userlevel_r=StuderUserLevel.VIEWONLY, userlevel_w=StuderUserLevel.VIEWONLY, nr_or_addr=2, name='a2', label='A2', unit='', data_type=StuderDataType.ENUM32,   size=2, access=StuderAccess.READ, target=StuderTarget.STANDARD, enum_id=2, enum_options={"0":"zero", "1":"one", "2":"two", "3":"three"})
TEST_DATAPOINT_BITFIELD = StuderDatapoint(family_id='aaa', parent_id='', id='a3', userlevel_r=StuderUserLevel.VIEWONLY, userlevel_w=StuderUserLevel.VIEWONLY, nr_or_addr=3, name='a3', label='A3', unit='', data_type=StuderDataType.BITFIELD, size=1, access=StuderAccess.READ, target=StuderTarget.STANDARD, enum_id=3, enum_options={"0":"zero", "1":"one", "2":"two", "4":"four"})


@pytest.mark.parametrize(
    "dp, key, exp_val, exp_except",
    [
        (TEST_DATAPOINT_ENUM32, 0,    'zero', None),
        (TEST_DATAPOINT_ENUM32, '0',  'zero', None),
        (TEST_DATAPOINT_ENUM32, 2,    'two',  None),
        (TEST_DATAPOINT_ENUM32, '2',  'two',  None),
        (TEST_DATAPOINT_ENUM32, 99,   '99',  None),
        (TEST_DATAPOINT_ENUM32, '99', '99',  None),
        (TEST_DATAPOINT_INT32, '1',    None, None),
        (TEST_DATAPOINT_BITFIELD, '1', None, None),
    ]
)
def test_enum_value(dp, key, exp_val, exp_except):
    if not exp_except:
        val = dp.enum_value(key)
        assert val == exp_val
    else:
        with pytest.raises(exp_except):
            val = dp.enum_value(key)


@pytest.mark.parametrize(
    "dp, val, exp_key, exp_except",
    [
        (TEST_DATAPOINT_ENUM32,   'zero', 0,    None),
        (TEST_DATAPOINT_ENUM32,   'two',  2,    None),
        (TEST_DATAPOINT_ENUM32,   'xx',   None, None),
        (TEST_DATAPOINT_INT32,    'one',  None, None),
        (TEST_DATAPOINT_BITFIELD, 'one',  None, None),
    ]
)
def test_enum_key(dp, val, exp_key, exp_except):
    if not exp_except:
        key = dp.enum_key(val)
        assert key == exp_key
    else:
        with pytest.raises(exp_except):
            key = dp.enum_key(val)


@pytest.mark.parametrize(
    "dp, key, exp_val, exp_except",
    [
        (TEST_DATAPOINT_BITFIELD, [],                   ['zero'],       None),
        (TEST_DATAPOINT_BITFIELD, [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],  ['zero'],       None),
        (TEST_DATAPOINT_BITFIELD, [False,True, False,False,False,False,False,False,False,False,False,False,False,False,False,False],  ['two'],        None),
        (TEST_DATAPOINT_BITFIELD, [True, True, False,False,False,False,False,False,False,False,False,False,False,False,False,False],  ['one','two'],  None),
        (TEST_DATAPOINT_INT32,    [],                   None,           None),
        (TEST_DATAPOINT_ENUM32,   [],                   None,           None),
        (TEST_DATAPOINT_BITFIELD, 99,                   None,           StuderParamException),
        (TEST_DATAPOINT_BITFIELD, '99',                 None,           StuderParamException),
    ]
)
def test_bitfield_value(dp, key, exp_val, exp_except):
    if not exp_except:
        val = dp.bitfield_value(key)
        assert val == exp_val
    else:
        with pytest.raises(exp_except):
            val = dp.bitfield_value(key)


@pytest.mark.parametrize(
    "dp, val, exp_key, exp_except",
    [
        (TEST_DATAPOINT_BITFIELD, ['zero'],       [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],                   None),
        (TEST_DATAPOINT_BITFIELD, ['zero'],       [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],  None),
        (TEST_DATAPOINT_BITFIELD, ['two'],        [False,True ,False,False,False,False,False,False,False,False,False,False,False,False,False,False],  None),
        (TEST_DATAPOINT_BITFIELD, ['one','two'],  [True, True, False,False,False,False,False,False,False,False,False,False,False,False,False,False],  None),
        (TEST_DATAPOINT_INT32,    ['two'],        None,  None),
        (TEST_DATAPOINT_ENUM32,   ['two'],        None,  None),
        (TEST_DATAPOINT_BITFIELD, 2,              None,  StuderParamException),
        (TEST_DATAPOINT_BITFIELD, 'two',          None,  StuderParamException),
    ]
)
def test_bitfield_key(dp, val, exp_key, exp_except):
    if not exp_except:
        key = dp.bitfield_key(val)
        assert key == exp_key
    else:
        with pytest.raises(exp_except):
            key = dp.bitfield_key(val)

