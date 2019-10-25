#!/usr/bin/env python
# license removed for brevity
import rospy
from autominy_msgs.msg import SpeedCommand, NormalizedSteeringCommand

def publish():
    pub_speed = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
    pub_steering = rospy.Publisher("/actuators/steering_normalized", NormalizedSteeringCommand, queue_size=10)

    steering_msg = NormalizedSteeringCommand()
    steering_msg.value = 1
    speed_msg = SpeedCommand()
    speed_msg.value = 0.3

    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub_steering.publish(steering_msg)
        pub_speed.publish(speed_msg)
        rospy.loginfo('speed is ' + str(speed_msg.value))
        print('speed is ' + str(speed_msg.value))
        rate.sleep()


if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass
