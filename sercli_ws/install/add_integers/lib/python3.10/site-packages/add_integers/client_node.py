import sys
import rclpy 
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts

class AdditionClientAsync(Node):
    def __init__(self):
        super().__init__("add_int_client_async")
        # Client olusturulur
        self.client = self.create_client(AddTwoInts, "add_two_ints")
        # Servisi bekler
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available")

    # Server'a gonderilecek istek
    def send_request(self):
        request = AddTwoInts.Request()
        request.a = int(sys.argv[1])
        request.b = int(sys.argv[2])
        self.future = self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    addition_client = AdditionClientAsync()
    addition_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(addition_client) # Node bir kez calisir
        if addition_client.future.done():
            try: 
                # istegin sonucunu alır.
                response = addition_client.future.result()
            except Exception as e:
                # istek basarisiz olursa hata mesaji verir.
                addition_client.get_logger().info(
                    f"Service call failed {e}"
                )
            else:
                # Sonucu verir.
                addition_client.get_logger().info(
                    f"Result of addition is {response.sum}"
                )
            break
    rclpy.shutdown() 

if __name__ == '__main__':
    main()
    