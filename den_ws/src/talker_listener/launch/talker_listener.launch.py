from launch import LaunchDescription
from launch_ros.actions import Node

TOPİC = "chatter" # Konu adi tanımlanır

def generate_launch_description():

    #Talker Node tanimlanir
    talker = Node(
        package="talker_listener",
        executable="talkerNode",
        name="talker_node",
        parameters=[{
            "topic": TOPİC
        }]
    )

    #Listener Node tanimlanir
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
