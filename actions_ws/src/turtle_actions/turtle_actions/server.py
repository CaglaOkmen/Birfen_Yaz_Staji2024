import rclpy 
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from turtlesim_interfaces.action import CountUntil 

class ServerNode(Node):
    def __init__(self):
        super().__init__("service")
        
        # Action Server başlatılıyor
        self.count_untill_service_ = ActionServer(
            self, CountUntil, "count_until", self.execute_callback)
        self.get_logger().info("Server is started")

        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10)
        
    def execute_callback(self, goal_handle: ServerGoalHandle):
        # get request from goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        # execute the action
        # Belirlenen süre kadar hareket ettir
        cmd = Twist()
        cmd.linear.x = 2.0
        self.get_logger().info("execute the goal")
        counter = 0
        for i in range(target_number):
            counter += 1
            self.get_logger().info(str(counter))
            self.cmd_vel_publisher_.publish(cmd)
            time.sleep(period)
           
        # one done, set goal final state
        goal_handle.succeed()
        self.ServerActive = False

        # and send the result
        result = CountUntil.Result()
        result.reached_number = counter
        return result     

def main(args=None):
    rclpy.init(args=args)
    addition_service = ServerNode()
    rclpy.spin(addition_service)
    addition_service.destroy_node()
    rclpy.shutdown() 

if __name__ == '__main__':
    main()
    