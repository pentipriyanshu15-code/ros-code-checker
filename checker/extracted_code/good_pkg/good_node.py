
import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('good_node')
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish("Hello Robot")
        rate.sleep()

if __name__ == '__main__':
    talker()
