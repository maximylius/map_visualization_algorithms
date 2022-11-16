"""Functions that help transforming 
"""

import os

import numpy as np
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
import matplotlib.pyplot as plt
import shapely
from shapely.geometry import Polygon, LineString, MultiLineString, Point, MultiPolygon, GeometryCollection
from shapely.affinity import translate, scale
from shapely.ops import cascaded_union
from pysolar.solar import get_altitude, get_azimuth
from datetime import datetime
import pandas as pd
import math
import pytz






















