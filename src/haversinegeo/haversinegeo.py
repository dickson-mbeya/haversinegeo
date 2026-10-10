import math


def haversine_distance(origin, destination):
  """Calculate the great-circle distance between two points on Earth.

  Uses the haversine formula to compute the shortest distance over the
  Earth's surface between two points given as latitude/longitude pairs,
  assuming a spherical Earth with a mean radius of 6,371,000 meters.

  Args:
    origin (tuple[float, float]): Starting point as ``(latitude, longitude)``
      in decimal degrees.
    destination (tuple[float, float]): End point as ``(latitude, longitude)``
      in decimal degrees.

  Returns:
    float: The distance between the two points in meters.

  Notes:
    - Coordinates must be in ``(latitude, longitude)`` order. Many GIS
      libraries use ``(longitude, latitude)``, so check the order of your
      data before calling.
    - Because the Earth is modelled as a perfect sphere, results can differ
      from ellipsoidal (e.g. WGS84) geodesic distances by up to roughly 0.5%.

  Examples:
    >>> haversine_distance((0, 0), (0, 0))
    0.0
    >>> round(haversine_distance((0, 0), (1, 0)), 2)
    111194.93
  """
  lat1, lon1 = origin
  lat2, lon2 = destination
  radius = 6371000
  dlat = math.radians(lat2-lat1)
  dlon = math.radians(lon2-lon1)
  a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
    * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  distance = radius * c
  return distance
