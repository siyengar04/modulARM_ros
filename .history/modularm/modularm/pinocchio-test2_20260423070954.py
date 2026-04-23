from robot_descriptions.loaders.pinocchio import load_robot_description

robot = load_robot_description("ur5_description")
model = robot.model
collision_model = robot.collision_model
visual_model = robot.visual_model
for name, function in robot.model.__class__.__dict__.items():
    print(" **** %s: %s" % (name, function.__doc__))
# Get index of end effector
 
idx = robot.index('wrist_3_joint')
 
# Compute and get the placement of joint number idx
 
placement = robot.placement(q, idx)
# Be carreful, Python always returns references to values.
# You can often .copy() the object to avoid side effects
# Only get the placement
placement = robot.data.oMi[idx].copy()