import numpy as np
from scipy.stats import multivariate_normal

#https://en.wikipedia.org/wiki/Earth_radius#Published_values
R = 6371.230

def gps_to_cartesian(coord):
    #https://stackoverflow.com/questions/1185408/converting-from-longitude-latitude-to-cartesian-coordinates
    lat, long = coord
    lat = np.deg2rad(lat)
    long = np.deg2rad(long)
    x = R * np.cos(lat) * np.cos(long)
    y = R * np.cos(lat) * np.sin(long)
    return x, y

def gaussian(mean, cov, input):
    return multivariate_normal(mean, cov).pdf(input)

class Simulation:

    def __init__(self):
        self.entities = [([0, 0],
                          [[100, 0],
                           [0, 100]],
                          0.9)] #(location, cov, risk_factor)

    def risk_field(self, coord):
        risk_level = 0
        coord = gps_to_cartesian(coord)
        for mean, cov, risk_factor in entities:
            risk_level += risk_factor * gaussian(mean, cov, coord)
        return risk_field
