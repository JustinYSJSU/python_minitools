import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class HeartbeatPublisherNode(Node):

    def __init__(self):
        super().__init__("heartbeat_publisher_node")
        self.pub = self.create_publisher(Bool, "heartbeat", 10)
        self.time = self.create_timer(0.5, self.generate_heartbeat_data)
    
    def generate_heartbeat_data(self):
        msg = Bool()
        msg.data = True

        self.pub.publish(msg=msg)