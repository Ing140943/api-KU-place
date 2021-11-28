# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.building_full import BuildingFull  # noqa: E501
from openapi_server.models.light_location import LightLocation  # noqa: E501
from openapi_server.models.pm_average import PMAverage  # noqa: E501
from openapi_server.models.security_img import SecurityImg  # noqa: E501
from openapi_server.models.security_location import SecurityLocation  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_average_pm(self):
        """Test case for controller_get_average_pm

        Provide the latitude and lontitude of light location
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/pmlocation/{location_id}'.format(location_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_building_detail(self):
        """Test case for controller_get_building_detail

        Return a name of location with their specific latitude and lontitude.
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/locations/{location_id}'.format(location_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_light_location(self):
        """Test case for controller_get_light_location

        Provide the latitude and lontitude of light location
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/lightlocation/{location_id}'.format(location_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_security_image(self):
        """Test case for controller_get_security_image

        Return a link of specifi security and provide their latitude and lontitude
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/securities/{security_id}'.format(security_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_security_location(self):
        """Test case for controller_get_security_location

        Provide the nearby light location and security location
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/securitylocation/{location_id}'.format(location_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
