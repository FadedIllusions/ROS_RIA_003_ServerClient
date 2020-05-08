#! /usr/bin/env python

# Import Needed Packages
import rospy
import rospkg
from std_srvs.srv import Empty, EmptyRequest


# Init Service Client Node And Wait For Service
rospy.init_node("service_move_bb8_in_circle_client")
rospy.wait_for_service("/move_bb8_in_circle")

# Instantiate Client Object -- Connection To Service
move_bb8_in_circle_service_client = rospy.ServiceProxy("/move_bb8_in_circle", Empty)

# Instantiate Request Object
move_bb8_in_circle_request_object = EmptyRequest()

result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object)
print result

rospy.spin()