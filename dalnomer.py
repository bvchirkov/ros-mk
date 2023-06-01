import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node('dalnomer')

def callback(scan):
    print(scan.ranges[0])

rospy.Subscriber("/scan", LaserScan, callback)
rospy.spin()
