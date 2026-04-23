from robot_descriptions.loaders.pinocchio import load_robot_description

robot = load_robot_description("ur5_description")
model = robot.model
collision_model = robot.collision_model
visual_model = robot.visual_model
for name, function in robot.model.__class__.__dict__.items():
    print(" **** %s: %s" % (name, function.__doc__))
