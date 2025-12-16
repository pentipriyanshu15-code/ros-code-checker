
import rospy, time
from sensor_msgs.msg import JointState

def move(pub,pos,msg):
    js = JointState()
    js.name = ["j1","j2","j3","j4","j5","j6"]
    js.position = pos
    rospy.loginfo(msg)
    pub.publish(js)
    time.sleep(2)

rospy.init_node("pick_place_node")
pub = rospy.Publisher("/joint_states", JointState, queue_size=10)
time.sleep(1)

move(pub,[0,0,0,0,0,0],"Home")
move(pub,[0.5,-0.8,1.2,0,0.5,0],"Pick")
move(pub,[0.5,-0.5,1.0,0,0.5,0],"Lift")
move(pub,[-0.5,-0.8,1.2,0,-0.5,0],"Place")
rospy.loginfo("SUCCESS")
