import math
class LagrangianMechanics:
    @staticmethod
    def lagrangian(kinetic_energy, potential_energy):
        return kinetic_energy - potential_energy

    @staticmethod
    def euler_lagrange(lagrangian, generalized_coordinate, generalized_velocity, time):
        pass

    @staticmethod
    def simple_pendulum_lagrangian(mass, length, angle, angular_velocity, g=9.81):
        kinetic_energy = 0.5 * mass * (length * angular_velocity) ** 2
        potential_energy = mass * g * length * (1 - math.cos(angle))
        return LagrangianMechanics.lagrangian(kinetic_energy, potential_energy)
