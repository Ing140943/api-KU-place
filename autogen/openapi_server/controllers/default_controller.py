import connexion
import six

from openapi_server.models.building_full import BuildingFull  # noqa: E501
from openapi_server.models.security_img import SecurityImg  # noqa: E501
from openapi_server.models.test_from_mark import TestFromMark  # noqa: E501
from openapi_server import util


def controller_get_building_detail(location_id):  # noqa: E501
    """Return a name of location with their specific latitude and lontitude.

     # noqa: E501

    :param location_id: 
    :type location_id: int

    :rtype: BuildingFull
    """
    return 'do some magic!'


def controller_get_sample():  # noqa: E501
    """Returns a list of basins.

     # noqa: E501


    :rtype: List[TestFromMark]
    """
    return 'do some magic!'


def controller_get_security_image(security_id):  # noqa: E501
    """Return a link of specifi security and provide their latitude and lontitude

     # noqa: E501

    :param security_id: 
    :type security_id: int

    :rtype: SecurityImg
    """
    return 'do some magic!'
