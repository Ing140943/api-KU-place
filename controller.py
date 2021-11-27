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

def get_light_location(location_id):
    cs = db.cursor()
    cs.execute("""SELECT kuPlace.building as building, light.lat as sensor_lat, light.lon as sensor_lon, light.time as time_light, light.light_value as value_light
                  FROM kuPlace INNER JOIN (SELECT location_id, TIMESTAMP(DATE(ts) , CONCAT(hour(ts), ':00:00')) as time, lat, lon, avg(light) as light_value
                  FROM kuLight
                  GROUP BY time, lat, lon, location_id) as light
                  WHERE kuPlace.id = light.location_id and kuPlace.id = %s""", [location_id])
    result = [models.LightLocation(building, sensor_lat, sensor_lon, time_light, value_light) for building, sensor_lat, sensor_lon, time_light, value_light in cs.fetchall()]
    cs.close()
    return result

def get_average_pm(location_id):
    cs = db.cursor()
    cs.execute("""SELECT kuPlace.building as building, kuPlace.lat as lat, kuPlace.lon as lon, pm.time as t, pm.avg_pm_per_day as average_pm
                  FROM kuPlace inner join
                  (SELECT location_id, TIMESTAMP(DATE(ts)) as time, lat, lon, AVG(pm) as avg_pm_per_day
                  FROM PM
                  GROUP BY time, lat, lon, location_id) as pm
                  where kuPlace.id = pm.location_id and kuPlace.id = %s""", [location_id])
    result = [models.PMAverage(building, lat, lon, t, average_pm) for building, lat, lon, t, average_pm in cs.fetchall()]
    cs.close()
    return result