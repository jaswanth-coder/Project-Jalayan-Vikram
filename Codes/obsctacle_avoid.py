'''obstacle Detection and Stop (obstacle_detection.py)
. When an obstacle is detected (within a specific distance), the robot will stop.'''
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan  # Message type for sensor data (e.g., LiDAR)
from geometry_msgs.msg import Twist

class ObstacleDetection(Node):
    def __init__(self):
        super().__init__('obstacle_detection')
        self.subscription = self.create_subscription(
            LaserScan, 'scan', self.scan_callback, 10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info("Obstacle detection node started...")

    def scan_callback(self, msg):
        min_distance = min(msg.ranges)  # Get the closest distance
        if min_distance < 0.5:  # Stop if obstacle is closer than 0.5 meters
            self.get_logger().info(f"Obstacle detected at {min_distance} meters!")
            self.stop_robot()

    def stop_robot(self):
        stop_msg = Twist()
        stop_msg.linear.x = 0.0  # Stop all movement
        stop_msg.angular.z = 0.0
        self.publisher_.publish(stop_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleDetection()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
