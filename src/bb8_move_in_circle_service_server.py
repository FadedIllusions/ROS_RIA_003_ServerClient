#! /usr/bin/env python

# Import Needed Packages
import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist


# Define Service Callback
def my_callback(request):
    rospy.loginfo("The Service bb8_move_in_circle Has Been Called")

    # Set Linear/Angular Rates
    move_circle.linear.x = 0.2
    move_circle.angular.z = 0.2

    # Publish move_circle Rates
    my_pub.publish(move_circle)

    rospy.loginfo("The Service bb8_move_in_circle Has Ended")

    return EmptyResponse()


# Init ROS Node
rospy.init_node('bb8_move_in_circle_server')

# Create Needed Service And Publisher
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

# Instantiate Twist Object
move_circle = Twist()

rospy.loginfo("Service bb8_move_in_circle Ready")

rospy.spin()