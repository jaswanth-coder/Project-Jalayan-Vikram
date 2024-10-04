from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='flood_robot',
            executable='move_robot',
            name='move_robot'
        ),
        Node(
            package='flood_robot',
            executable='obstacle_detection',
            name='obstacle_detection'
        )
    ])
