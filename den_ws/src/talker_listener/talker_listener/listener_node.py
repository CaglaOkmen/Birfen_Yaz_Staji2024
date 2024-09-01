import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__("listener_node")

        # Parametre ayarlanir ve degeri tanimlanir.
        self.declare_parameter("topic", value="talker_topic")
        topic_name = self.get_parameter("topic").get_parameter_value().string_value

        # Subscription (Abone) tanımlanır. String turinde mesajlari alir
        self.subscription = self.create_subscription(
            String, topic_name, self.listener_callback, 10)

    # Aldigi mesaji loglar
    def listener_callback(self, msg):
        self.get_logger().info(f"Received {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    listener_node = ListenerNode() 
    rclpy.spin(listener_node)
    listener_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
