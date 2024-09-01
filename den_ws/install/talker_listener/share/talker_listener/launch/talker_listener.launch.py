from launch import LaunchDescription
from launch_ros.actions import Node

TOPİC = "chatter"

def generate_launch_description():
    talker = Node(
        package="talker_listener",
        executable="talkerNode",
        name="talker_node",
        parameters=[{
            "topic": TOPİC
        }]
    )

    listener = Node(
        package="talker_listener",
        executable="listenerNode",
        name="listener_node",
        parameters=[{
            "topic": TOPİC
        }]
    )

    # Başlatılacak düğümler
    return LaunchDescription([
        talker,
        listener
    ])
