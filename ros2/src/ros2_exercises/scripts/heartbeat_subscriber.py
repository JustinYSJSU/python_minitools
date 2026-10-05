import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Bool

class HeartbeatSubscriberNode(Node):

    def __init__(self):
        super().__init__("heartbeat_subscriber_node")
        self.sub = self.create_subscription(Bool, "heartbeat", self.heartbeat_callback, 10)
        self.declare_parameter("timeout_seconds", 2.0)
        self.declare_parameter("check_period", 0.5)

        self.last_heartbeat = None
        self.timeout_timer = self.create_timer(self.get_parameter("check_period").value, self.check_period)

    def heartbeat_callback(self, msg):
        if not msg:
            print("message not received")
        else:
            print(f"message data: {msg.data}")
            self.last_heartbeat = time.time()
    
    def check_period(self):

        if self.last_heartbeat is None:
            print("no heartbeat received yet")
            return
            
        elapsed = time.time() - self.last_heartbeat
        return elapsed > self.get_parameter("timeout_seconds").value

def main():
    rclpy.init() # initialize ros2 communication
    my_sub = HeartbeatSubscriberNode()
    print("Subscribing")

try:
    rclpy.spin(my_sub) # run until interrupt via keyboard
except KeyboardInterrupt:
    print("Terminating node...")
    my_sub.destroy_node()

if __name__ == '__main__':
        main()