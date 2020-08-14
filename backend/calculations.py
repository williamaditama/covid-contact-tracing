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

# TODO: turn this into a sum of the gaussians
def risk_field(coord):
    return 0

def gaussian(mean, cov, input):
    return multivariate_normal(mean, cov).pdf(input)
