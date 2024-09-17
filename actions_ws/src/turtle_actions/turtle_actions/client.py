import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.action.client import ClientGoalHandle
from turtlesim_interfaces.action import CountUntil 

class ClientNode(Node):
    def __init__(self):
        super().__init__("client")
        # Action Client oluşturulur
        self.count_untill_client_ = ActionClient(
            self, CountUntil, "count_until")
        self.get_logger().info("Action client is started")
        

    def send_goal(self,target_number, period):
        # wait for the server
        self.count_untill_client_.wait_for_server()

        # create a goal
        goal = CountUntil.Goal()
        goal.target_number =target_number
        goal.period = period

        # send the goal
        self.get_logger().info("sending goal")
        self.count_untill_client_.send_goal_async(goal).\
            add_done_callback(self.goal_response_callback)
        
    # Sunucudan gelen yanıt işlenir
    def goal_response_callback(self, future):
        self.goal_handle_ = ClientGoalHandle.future.result()
        if self.goal_handle_.accepted:
            self.goal_handle_.get_result_async().\
                add_done_callback(self.goal_result_callback)
            
    # Sunucudan gelen sonuç işlenir
    def goal_result_callback(self, future):
        result = future.result().result
        self.get_logger().info("Result: " + str(result.reached_number))

def main(args=None):
    rclpy.init(args=args)
    node = ClientNode()
    node.send_goal(2, 1.0) # Hedef gönderir
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    