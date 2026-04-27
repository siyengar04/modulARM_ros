from robot_descriptions.loaders.pinocchio import load_robot_description

robot = load_robot_description(
    "/home/samee/ros2_modulARM/src/modularm/description/robot_description.urdf"
)
model = robot.model
collision_model = robot.collision_model
visual_model = robot.visual_model
for name, function in robot.model.__class__.__dict__.items():
    print(" **** %s: %s" % (name, function.__doc__))
# Get index of end effector

idx = robot.index("wrist_3_joint")

# Compute and get the placement of joint number idx

placement = robot.placement(q, idx)
# Be carreful, Python always returns references to values.
# You can often .copy() the object to avoid side effects
# Only get the placement
placement = robot.data.oMi[idx].copy()
q = zero(robot.nq)
v = rand(robot.nv)
robot.com(q)  # Compute the robot center of mass.
robot.placement(q, 3)  # Compute the placement of joint 3
robot.initViewer(loadModel=True)
