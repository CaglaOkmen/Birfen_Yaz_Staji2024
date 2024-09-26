#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from custom_interfaces.srv import MyBool
from custom_interfaces.msg import TargetCor

class CombineNode(Node):

    def __init__(self):
        super().__init__('combine_node')

        self.timer_duration = 5.0 

        self.cmd_vel_publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.target_cor_publisher_ = self.create_publisher(TargetCor, '/target', 10)
        
        self.pose_subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        
        self.service = self.create_service(MyBool, '/start', self.srv_callback)

        self.service_active = False  
        self.get_logger().info('Turtle controller has been started')

    def srv_callback(self, request, response):
        if request.x:
            self.get_logger().info('Starting')
            self.service_active = True
            response.success = True
        else:
            self.get_logger().info('Stopped')
            self.service_active = False
            response.success = False

        return response

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        
        if self.service_active: 
            msg = TargetCor()
            if pose.x > 10.9 or pose.y > 10.9 or pose.x < 0.09 or pose.y < 0.09:
                msg.uyari = "Sinira geldi"
                self.target_cor_publisher_.publish(msg)

                self.get_logger().info(f'publishing: {msg.uyari}')
                if 0.0 < self.timer_duration:
                    cmd.linear.x = 0.0
                    cmd.angular.z = 2.0
                    self.timer_duration -= 1
                else:
                    self.timer_duration = 20.0 
                    cmd.linear.x = 5.0
                    cmd.angular.z = 0.0
            else:
                cmd.linear.x = 5.0
                cmd.angular.z = 0.0
            
            self.cmd_vel_publisher_.publish(cmd)

    


def main(args=None):
    rclpy.init(args=args)
    node = CombineNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()