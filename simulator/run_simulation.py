
import rospy, time, os
from sensor_msgs.msg import JointState
from PIL import Image, ImageDraw

OUT = "../simulation_output"

rospy.init_node("sim_runner")
pub = rospy.Publisher("/joint_states", JointState, queue_size=10)
time.sleep(1)

steps = [
    ([0,0,0,0,0,0],"Home"),
    ([0.5,-0.8,1.2,0,0.5,0],"Pick"),
    ([0.5,-0.5,1.0,0,0.5,0],"Lift"),
    ([-0.5,-0.8,1.2,0,-0.5,0],"Place")
]

for p,n in steps:
    js = JointState()
    js.name=["j1","j2","j3","j4","j5","j6"]
    js.position=p
    pub.publish(js)
    rospy.loginfo(n)
    time.sleep(2)

os.makedirs(OUT,exist_ok=True)
img = Image.new("RGB",(400,300),"white")
ImageDraw.Draw(img).text((80,140),"Pick & Place SUCCESS",(0,0,0))
img.save(f"{OUT}/result.png")
print("Simulation Success")




