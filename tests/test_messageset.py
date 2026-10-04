import pytest
import pytest_asyncio

from pystudershared import StuderMessageDef, StuderMessageSet
from pystudershared import StuderUserLevel
from pystudershared import StuderMessageUnknownException


TEST_MESSAGESET = StuderMessageSet([
    StuderMessageDef(level=StuderUserLevel.VIEWONLY, number=1, string='one'),
    StuderMessageDef(level=StuderUserLevel.VIEWONLY, number=2, string='two'),
    StuderMessageDef(level=StuderUserLevel.VIEWONLY, number=3, string='three'),
])


@pytest.mark.parametrize(
    "number, exp_number, exp_string, exp_except",
    [
        (2,    2,    'two', None),
        (99,   None, None,  StuderMessageUnknownException),
        (None, None, None,  StuderMessageUnknownException),
    ]
)
def test_get_by_nr(number, exp_number, exp_string, exp_except):
    messageset = TEST_MESSAGESET

    if not exp_except:
        msg = messageset.get_by_nr(number)
        assert msg is not None
        assert msg.number == exp_number
        assert msg.string == exp_string
    else:
        with pytest.raises(exp_except):
            msg = messageset.get_by_nr(number)


@pytest.mark.parametrize(
    "number, exp_string, exp_except",
    [
        (2,    'two', None),
        (99,   None,  StuderMessageUnknownException),
        (None, None,  StuderMessageUnknownException),
    ]
)
def test_str_by_nr(number, exp_string, exp_except):
    messageset = TEST_MESSAGESET

    if not exp_except:
        string = messageset.str_by_nr(number)
        assert string is not None
        assert string == exp_string
    else:
        with pytest.raises(exp_except):
            string = messageset.str_by_nr(number)


