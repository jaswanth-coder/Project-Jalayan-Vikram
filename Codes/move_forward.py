'''Basic Robot Movement Controller (move_robot.py)
This script will control the robot’s movement by publishing commands to a topic that ROS2 nodes can subscribe to.'''

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist  # Message type for robot velocity

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.move_forward)
        self.get_logger().info("Robot is ready to move forward...")

    def move_forward(self):
        msg = Twist()
        msg.linear.x = 0.5  # Move forward at 0.5 m/s
        msg.angular.z = 0.0  # No turning
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    robot = MoveRobot()
    rclpy.spin(robot)
    robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
