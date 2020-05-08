# ROS_RIA_003_ServerClient

<p align="center">
  <img src="/images/bb8_circle.gif" alt="BB8 Circle GIF">
</p>


This repository is a simple service server/client pair, with accompanying launch files, to have the Sphero BB8 traverse in a circle.

<p align="center">
  <img src="/images/service_publisher.png" alt="Service/Publisher Code Excerpt">
</p>

As seen in the code, when subscribed to by a client, the server responds to requests by publishing Twist messages for linear.x and angular.z values to /cmd_vel.
