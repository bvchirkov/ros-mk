import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

rospy.init_node('dalnomer')
target = 0.3
vel = Twist()
pub = rospy.Publisher("cmd_vel", Twist, queue_size = 1)

def callback(scan):
    if scan.ranges[0] > target:
        vel.linear.x = 0.1
    else:
        vel.linear.x = 0
    
    pub.publish(vel)

rospy.Subscriber("/scan", LaserScan, callback)
rospy.spin()
