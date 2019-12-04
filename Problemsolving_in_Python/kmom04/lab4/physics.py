'''mod'''
def free_fall(time, speed=0, gravity=9.82):
    ''' function '''
    speed = speed + gravity*time
    return speed

def gravitational_pull(m1, m2, r):
    ''' function '''
    g = 6.674*10**-11
    force = (g * m1 * m2) / (r**2)
    return force
