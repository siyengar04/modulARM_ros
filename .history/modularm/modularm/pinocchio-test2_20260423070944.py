from robot_descriptions.loaders.pinocchio import load_robot_description

robot = load_robot_description("ur5_description")
model = robot.model
collision_model = robot.collision_model
visual_model = robot.visual_model
