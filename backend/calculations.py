import numpy as np
from scipy.stats import multivariate_normal
import db_interface
import time
import math

#https://en.wikipedia.org/wiki/Earth_radius#Published_values
R = 6371.230

default_cov = [[1, 0],
               [0, 1]]

def gps_to_cartesian(coord):
    #https://stackoverflow.com/questions/1185408/converting-from-longitude-latitude-to-cartesian-coordinates
    lat, long = coord
    lat = np.deg2rad(lat)
    long = np.deg2rad(long)
    x = R * np.cos(lat) * np.cos(long)
    y = R * np.cos(lat) * np.sin(long)
    return x*100, y*100 #x and y are in hectometer(100) originally

def gaussian(mean, cov, input):
    # scale by 2 * math.pi to get a max value of 1 at the mean
    # however this is no longer a valid probability distribution
    return 2 * math.pi * multivariate_normal(mean, cov).pdf(input)

class Simulation:
    """
    store all (xi, yi), ti

    Erase all records with ti's after a week or sth.

    current time = ct
    K = decay constant

    Risk Level at (X, Y at ct) = sum up all K/(ct - ti) * gaussian(input = [X, Y], mean = [xi, yi], cov) + (individual specific term)

    The higher the persistence, the lesser the decay
    """

    def __init__(self, persistence=100.0):
        self.persistence = persistence

    def get_entities(self):
        rows = db_interface.get_loc()
        #assume covariance = [[1, 1], [1, 1]]
        return [(gps_to_cartesian((float(lat), float(long))), default_cov, time) for _, lat, long, time in rows]

    def risk_field(self, coord):
        risk_level = 0.0
        coord = gps_to_cartesian(coord)
        curr_time = time.time()
        for mean, cov, start_time in self.get_entities():
            decay_term = self.persistence/(curr_time - start_time + 1e-8)
            risk_level += decay_term * gaussian(mean, cov, coord)
        return risk_level
