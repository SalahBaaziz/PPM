import math
class WorkEnergy:
    @staticmethod
    def work_done(force, displacement, angle=0):
        return force * displacement * math.cos(math.radians(angle))

    @staticmethod
    def kinetic_energy(mass, velocity):
        return 0.5 * mass * velocity ** 2

    @staticmethod
    def rotational_kinetic_energy(moment_of_inertia, angular_velocity):
        return 0.5 * moment_of_inertia * angular_velocity ** 2
