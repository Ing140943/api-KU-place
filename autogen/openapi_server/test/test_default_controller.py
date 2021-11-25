# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.basin_full import BasinFull  # noqa: E501
from openapi_server.models.basin_short import BasinShort  # noqa: E501
from openapi_server.models.station_full import StationFull  # noqa: E501
from openapi_server.models.station_short import StationShort  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_basin_details(self):
        """Test case for controller_get_basin_details

        Returns complete details of the specified basin
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/basins/{basin_id}'.format(basin_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_basins(self):
        """Test case for controller_get_basins

        Returns a list of basins.
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/basins',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_station_details(self):
        """Test case for controller_get_station_details

        Returns complete details of the specified station
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/stations/{station_id}'.format(station_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_stations(self):
        """Test case for controller_get_stations

        Returns a list of stations located within the specified basin.
        """
        headers = { 
        }
        response = self.client.open(
            '/rain-api/v1/basins/{basin_id}/stations'.format(basin_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
