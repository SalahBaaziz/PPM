# interactive_main.py
from dimensional_analysis import DimensionalAnalysis
from kinematics import RigidBodyKinematics
from work_energy import WorkEnergy
from lagrangian_mechanics import LagrangianMechanics


def get_float_input(prompt):
    return float(input(prompt))


def dimensional_analysis_interaction():
    quantity = get_float_input("Enter the quantity: ")
    units = input("Enter the units (e.g., m/s, kg): ")
    analysis = DimensionalAnalysis(quantity, units)
    target_units = input("Enter the target units for conversion: ")
    converted = analysis.convert_to(target_units)
    print(f"Converted value: {converted}")


def kinematics_interaction():
    print("Choose an option:")
    print("1. Calculate angular velocity")
    print("2. Calculate pendulum motion")
    print("3. Calculate damped pendulum motion")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        initial_velocity = get_float_input("Enter the initial angular velocity (rad/s): ")
        angular_acceleration = get_float_input("Enter the angular acceleration (rad/s²): ")
        time = get_float_input("Enter the time (s): ")
        result = RigidBodyKinematics.angular_velocity(initial_velocity, angular_acceleration, time)
        print(f"Angular velocity: {result} rad/s")
    elif choice == '2':
        length = get_float_input("Enter the length of the pendulum (m): ")
        initial_angle = get_float_input("Enter the initial angle (radians): ")
        time = get_float_input("Enter the time (s): ")
        result = RigidBodyKinematics.pendulum_motion(length, initial_angle, time)
        print(f"Pendulum angle: {result} radians")
    elif choice == '3':
        length = get_float_input("Enter the length of the pendulum (m): ")
        initial_angle = get_float_input("Enter the initial angle (radians): ")
        damping_coefficient = get_float_input("Enter the damping coefficient: ")
        time = get_float_input("Enter the time (s): ")
        result = RigidBodyKinematics.damped_pendulum_motion(length, initial_angle, damping_coefficient, time)
        print(f"Damped pendulum angle: {result} radians")


def work_energy_interaction():
    print("Choose an option:")
    print("1. Calculate work done")
    print("2. Calculate kinetic energy")
    print("3. Calculate rotational kinetic energy")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        force = get_float_input("Enter the force (N): ")
        displacement = get_float_input("Enter the displacement (m): ")
        angle = get_float_input("Enter the angle between force and displacement (degrees): ")
        result = WorkEnergy.work_done(force, displacement, angle)
        print(f"Work done: {result} J")
    elif choice == '2':
        mass = get_float_input("Enter the mass (kg): ")
        velocity = get_float_input("Enter the velocity (m/s): ")
        result = WorkEnergy.kinetic_energy(mass, velocity)
        print(f"Kinetic energy: {result} J")
    elif choice == '3':
        moment_of_inertia = get_float_input("Enter the moment of inertia (kg·m²): ")
        angular_velocity = get_float_input("Enter the angular velocity (rad/s): ")
        result = WorkEnergy.rotational_kinetic_energy(moment_of_inertia, angular_velocity)
        print(f"Rotational kinetic energy: {result} J")


def lagrangian_mechanics_interaction():
    print("Choose an option:")
    print("1. Calculate Lagrangian")
    print("2. Calculate simple pendulum Lagrangian")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        kinetic_energy = get_float_input("Enter the kinetic energy (J): ")
        potential_energy = get_float_input("Enter the potential energy (J): ")
        result = LagrangianMechanics.lagrangian(kinetic_energy, potential_energy)
        print(f"Lagrangian: {result}")
    elif choice == '2':
        mass = get_float_input("Enter the mass (kg): ")
        length = get_float_input("Enter the length (m): ")
        angle = get_float_input("Enter the angle (radians): ")
        angular_velocity = get_float_input("Enter the angular velocity (rad/s): ")
        result = LagrangianMechanics.simple_pendulum_lagrangian(mass, length, angle, angular_velocity)
        print(f"Simple pendulum Lagrangian: {result}")


def main():
    while True:
        print("\nChoose a module to use:")
        print("1. Dimensional Analysis")
        print("2. Rigid Body Kinematics")
        print("3. Work and Energy")
        print("4. Lagrangian Mechanics")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            dimensional_analysis_interaction()
        elif choice == '2':
            kinematics_interaction()
        elif choice == '3':
            work_energy_interaction()
        elif choice == '4':
            lagrangian_mechanics_interaction()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
