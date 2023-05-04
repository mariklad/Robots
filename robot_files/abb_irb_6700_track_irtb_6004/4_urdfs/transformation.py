# Update the track data for the URDF process

from compas.geometry import Rotation
import math
# track calibration quaternion matrix from Robot Backup MOC.cfg
track_parameter = Rotation.from_quaternion([1, -0.000156286, -0.000156286,0.000221566])
# translate to URDF RPY formate
eluer_angle_r = track_parameter.euler_angles(True, 'xyz')
# print to confirm (in radians)
print("rpy value", eluer_angle_r)

eluer_angle_d = [i/math.pi*180 for i in eluer_angle_r]
# print to confirm (in degress)
print(eluer_angle_d)