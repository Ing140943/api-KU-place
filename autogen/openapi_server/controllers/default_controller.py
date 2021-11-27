import connexion
import six

from openapi_server.models.building_full import BuildingFull  # noqa: E501
from openapi_server.models.light_location import LightLocation  # noqa: E501
from openapi_server.models.pm_average import PMAverage  # noqa: E501
from openapi_server.models.security_img import SecurityImg  # noqa: E501
from openapi_server.models.security_location import SecurityLocation  # noqa: E501
from openapi_server import util


def controller_get_average_pm(location_id):  # noqa: E501
    """Provide the latitude and lontitude of light location

     # noqa: E501

    :param location_id: 
    :type location_id: int

    :rtype: PMAverage
    """
    return 'do some magic!'


def controller_get_building_detail(location_id):  # noqa: E501
    """Return a name of location with their specific latitude and lontitude.

     # noqa: E501

    :param location_id: 
    :type location_id: int

    :rtype: BuildingFull
    """
    return 'do some magic!'


def controller_get_light_location(location_id):  # noqa: E501
    """Provide the latitude and lontitude of light location

     # noqa: E501

    :param location_id: 
    :type location_id: int

    :rtype: LightLocation
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


def controller_get_security_location(location_id):  # noqa: E501
    """Provide the nearby light location and security location

     # noqa: E501

    :param location_id: 
    :type location_id: int

    :rtype: SecurityLocation
    """
    return 'do some magic!'
