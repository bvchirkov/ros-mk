import rospy
import math
from nav_msgs.msg import Odometry

rospy.init_node('transportir')

def callback(odom):
    theta = 2*math.degrees(math.asin(odom.pose.pose.orientation.z)*math.copysign(1,odom.pose.pose.orientation.w))
    print(theta)
    
rospy.Subscriber("/odom", Odometry, callback)
rospy.spin()
