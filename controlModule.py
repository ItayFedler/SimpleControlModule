# from pydoc import describe
# from tkinter import N
"""import packages for testing"""
import tkinter as tk
import tkinter.ttk as ttk


# This is the class that will be used to control the robot.

"""define vector of trajectories to be used in the control module"""
class Trajectory:
    def __init__(self, x, y, z, theta):
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta
        #self.time = time.time()
        #"""get the time when the trajectory is created"""  

"""define promise that the trajectory is resolved"""

class PromiseTrajectory:
    resolved = False
    def __init__(self, trajectory):
        self.trajectory = trajectory
        self.resolved = False
    def resolve(self):
        self.resolved = True
        return self.trajectory
    def isResolved(self):
        return self.resolved

"""define model predictive controller"""
class MPC:
    constraint_1 = None
    def __init__(self):
        """fill constraint with only trajectory resolved"""
        self.constraint_1 =PromiseTrajectory(Trajectory(0,0,0,0))
    def run(self):
        """run the model predictive controller and execute steering subsystem"""
        if self.constraint_1.isResolved():
            SteeringSubsystem.execute(self.constraint_1.resolve())
            BrakeSubsystem.execute(self.constraint_1.resolve())

        else:
            return None

"""create a steering subsystem"""
class SteeringSubsystem:
    def execute(self, steering_command):
        """apply steering_command to Steering wheel controller"""
        self.Steering_wheel_controller.apply(steering_command)
    class Steering_wheel_controller:
        def apply(self, steering_command):
            """apply steering_command to steering wheel"""
            self.steering_wheel.apply(steering_command)
            return steering_command
        


""""create a brake subsystem"""
class BrakeSubsystem:
    def execute(self, speed):
        """apply speed to Acceleration controller"""
        self.Acceleration_controller.apply(speed)
    class Acceleration_controller:
        sensoreReadPromise = None
        def __init__(self,promiseSensor):
            self.sensoreReadPromise = promiseSensor

        def apply(self, speed):
            """if sensoread is resolved PromiseSensor get the value"""
            if self.sensoreread.isResolved():
                sensor_read = self.sensoreread.resolve()
                """create function that clculate the error between the speed and the sensor read
                and make condition when absulte value of the error is greater than 0.1
                run Brake pedal controller and Electric motor controller"""
                error = abs(speed - sensor_read)
                if error > 0.1:
                    self.Brake_pedal_controller.apply(speed)
                    self.Electric_motor_controller.apply(speed)
                    
                    
            return speed

"""define sensor promise"""
class PromiseSensor:
    resolved = False
    sensor_value = None
    def __init__(self, ):
        self.resolved = False
    def resolve(self,sensor_value):
        self.resolved = True
        self.sensor_value = sensor_value
    def isResolved(self):
        return self.resolved

"""add observer to the sensor"""
class Sensor:
    def __init__(self):
        self.sensor_read = PromiseSensor()
    def read(self):
        """read the sensor and return the promise"""
        return self.sensor_read