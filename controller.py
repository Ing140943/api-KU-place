import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

db = mysql.connect(host=DB_HOST,
                   user=DB_USER,
                   passwd=DB_PASSWD,
                   db=DB_NAME)


def get_sample():
    cs = db.cursor()
    cs.execute("""SELECT light, deviceId
                  FROM KuLight""")
    result = [models.TestFromMark(light) for light, deviceId in cs.fetchall()]
    cs.close()
    return result


def get_building_detail(location_id):
    cs = db.cursor()
    cs.execute("""SELECT building,lat,lon
                  FROM kuPlace
                  WHERE id = %s""", [location_id])
    result = cs.fetchone()
    cs.close()
    if result:
        building, lat, lon = result
        return models.BuildingFull(building, lat, lon)
    else:
        abort(404)


def get_security_image(security_id):
    cs = db.cursor()
    cs.execute("""SELECT img_link, lat, lon
                  FROM kuSecurity
                  WHERE id = %s""", [security_id])
    result = cs.fetchone()
    cs.close()
    if result:
        img_link, lat, lon = result
        return models.SecurityImg(img_link, lat, lon)
    else:
        abort(404)

def get_security_location(location_id):
    cs = db.cursor()
    cs.execute("""SELECT building, security_id as security_post_id, img_link, s.lat as lat, s.lon as lon,distance
                  FROM kuPlace as p inner join kuSecurity as s
                  on s.location_id = p.id
                  where p.id = %s
                  ORDER BY p.id""", [location_id])
    result = [models.SecurityLocation(building, security_post_id, img_link, lat, lon, distance) for building, security_post_id, img_link, lat, lon, distance in cs.fetchall()]
    cs.close()
    return result

def get_basins():
    cs = db.cursor()
    cs.execute("SELECT basin_id,ename FROM basin")
    result = [models.BasinShort(basin_id, name) for basin_id, name in cs.fetchall()]
    cs.close()
    return result


def get_basin_details(basin_id):
    cs = db.cursor()
    cs.execute("""
        SELECT basin_id, ename, area
        FROM basin
        WHERE basin_id=%s
        """, [basin_id])
    result = cs.fetchone()
    cs.close()
    if result:
        basin_id, name, area = result
        return models.BasinFull(basin_id, name, area)
    else:
        abort(404)


def get_stations(basin_id):
    cs = db.cursor()
    cs.execute("""
        SELECT station_id, s.ename
        FROM station s
        INNER JOIN basin b ON ST_CONTAINS(b.geometry, POINT(s.lon, s.lat))
        WHERE basin_id=%s
        """, [basin_id])
    result = [models.StationShort(station_id, name) for station_id, name in cs.fetchall()]
    cs.close()
    return result


def get_station_details(station_id):
    cs = db.cursor()
    cs.execute("""
        SELECT station_id, basin_id, s.ename, s.lat, s.lon
        FROM station s
        INNER JOIN basin b ON ST_CONTAINS(b.geometry, POINT(s.lon, s.lat))
        WHERE station_id=%s
        """, [station_id])
    result = cs.fetchone()
    cs.close()
    if result:
        station_id, basin_id, name, lat, lon = result
        return models.StationFull(station_id, basin_id, name, lat, lon)
    else:
        abort(404)


def get_annual_rainfalls(basin_id, year):
    cs = db.cursor()
    cs.execute("""
     SELECT SUM(daily)
     FROM (
        SELECT AVG(r.amount) as daily
        FROM rainfall r
        INNER JOIN station s ON s.station_id=r.station_id
        INNER JOIN basin b ON ST_CONTAINS(b.geometry, POINT(s.lon, s.lat))
        WHERE b.basin_id=%s AND r.year=%s
        GROUP BY b.basin_id, r.year, r.month, r.day) daily""", [basin_id, year])
    result = cs.fetchone()
    cs.close()
    if result:
        return models.StationAnual(basin_id, year, result[0])
    else:
        abort(404)
