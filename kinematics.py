
import math

class RigidBodyKinematics:
    @staticmethod
    def angular_velocity(initial_velocity, angular_acceleration, time):
        return initial_velocity + angular_acceleration * time

    @staticmethod
    def pendulum_motion(length, initial_angle, time, g=9.81):
        angular_frequency = math.sqrt(g / length)
        return initial_angle * math.cos(angular_frequency * time)

    @staticmethod
    def damped_pendulum_motion(length, initial_angle, damping_coefficient, time, g=9.81):
        angular_frequency = math.sqrt(g / length)
        damped_frequency = math.sqrt(angular_frequency**2 - (damping_coefficient / 2)**2)
        return initial_angle * math.exp(-damping_coefficient * time / 2) * math.cos(damped_frequency * time)
