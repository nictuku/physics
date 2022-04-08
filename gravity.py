import numpy

G = 6.67*10**-11   # m^3 / (kg s^2)  => what is s?

def force_of_gravity(mass_object_1, mass_object_2, distance):
    return G * mass_object_1 * mass_object_2 / (distance**2)

earth_mass = 5.97*10**24 # kg
sun_mass = 1.99*10**30  # kg
earth_sun_distance = 1.5*10**11 # m

print("How large is grav force of Sun on Earth: %.1E" % force_of_gravity(earth_mass, sun_mass, earth_sun_distance))
