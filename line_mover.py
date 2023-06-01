import rospy, math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

rospy.init_node('line_mover')

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
pub_vel = Twist()
pub_vel.linear.x = 0.05 #будем всегда ехать вперед

def quaternion_to_theta(odom):
    return(2*(math.asin(odom.pose.pose.orientation.z)*math.copysign(1,odom.pose.pose.orientation.w)))

def odomcb(odom):
    theta = quaternion_to_theta(odom)
    pub_vel.angular.z = - theta
    pub.publish(pub_vel)

rospy.Subscriber("/odom", Odometry, odomcb)
rospy.spin()
