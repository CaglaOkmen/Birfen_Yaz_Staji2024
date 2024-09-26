#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from custom_interfaces.srv import MyBool
from custom_interfaces.msg import TargetCor

class CombineNode(Node):

    def __init__(self):
        # Node sınıfının initializer'ını çağır ve "combine_node" adında bir node oluştur
        super().__init__('combine_node')

        # Başlangıç zamanlayıcı süresi (turtle yön değiştirirken kullanılır)
        self.timer_duration = 5.0 

        # Hız komutlarını yayınlayacak publisher oluştur
        self.cmd_vel_publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Hedef koordinatları yayınlayacak publisher oluştur
        self.target_cor_publisher_ = self.create_publisher(TargetCor, '/target', 10)
        
        # Turtle pozisyonunu almak için subscriber oluştur
        self.pose_subscriber_ = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        
        # Servis oluşturur başlatmak ve durdurmak icin
        self.service = self.create_service(MyBool, '/start', self.srv_callback)

        # Servisin aktif olup olmadığını kontrol etmek için bir bayrak
        self.service_active = False  
        self.get_logger().info('Turtle controller has been started')

    def srv_callback(self, request, response):
        # Servis isteğine göre servisi başlat veya durdur
        if request.x:
            self.get_logger().info('Starting')
            self.service_active = True
            response.success = True
        else:
            self.get_logger().info('Stopped')
            self.service_active = False
            response.success = False

        # Servis sonucunu geri döndür
        return response

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        
        # Servis aktif olduğunda turtle hareket etmeye başlar
        if self.service_active: 
            msg = TargetCor()
            # Turtle sınır değerlerine ulaştığında uyarı mesajı yayınla
            if pose.x > 10.9 or pose.y > 10.9 or pose.x < 0.09 or pose.y < 0.09:
                msg.uyari = "Sinira geldi"
                self.target_cor_publisher_.publish(msg)

                self.get_logger().info(f'publishing: {msg.uyari}')
                # Turtle sınırda ise yön değiştirme işlemi başlar
                if 0.0 < self.timer_duration:
                    cmd.linear.x = 0.0  # Durma
                    cmd.angular.z = 2.0  # Dönme
                    self.timer_duration -= 1
                else:
                    # Süre dolduğunda ileriye doğru gitmeye devam et
                    self.timer_duration = 20.0 
                    cmd.linear.x = 5.0  # İleri gitme
                    cmd.angular.z = 0.0  # Dönmeyi durdurma
            else:
                # Turtle sınırda değilse düz ilerle
                cmd.linear.x = 5.0
                cmd.angular.z = 0.0
            
            # Hız komutunu yayınla
            self.cmd_vel_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = CombineNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
