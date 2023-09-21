#rudimentary MuJoCo mjcf to ROS URDF converter using the UrdfEditor

from pybullet_utils import bullet_client as bc
import pybullet_data as pd

import pybullet_utils.urdfEditor as ed


if __name__ == "__main__":
    # mjcf_path = "/home/chenbao/Desktop/projects/robel/robel/robel-scenes/dclaw/dclaw3xh.xml"
    mjcf_path = "/home/chenbao/Desktop/projects/robel/robel/robel-scenes/dclaw/dclaw3xh_change.xml"

    # mjcf_path = "/home/chenbao/Desktop/projects/robel/robel/robel-scenes/dclaw/assets/chain3xh.xml"

    p = bc.BulletClient()
    p.setAdditionalSearchPath(pd.getDataPath())
    objs = p.loadMJCF(mjcf_path, flags=p.URDF_USE_IMPLICIT_CYLINDER)

    for o in objs:
      #print("o=",o, p.getBodyInfo(o), p.getNumJoints(o))
      humanoid = objs[o]
      ed0 = ed.UrdfEditor()
      ed0.initializeFromBulletBody(humanoid, p._client)
      robotName = str(p.getBodyInfo(o)[1], 'utf-8')
      partName = str(p.getBodyInfo(o)[0], 'utf-8')

      print("robotName=", robotName)
      print("partName=", partName)

      saveVisuals = False
      ed0.saveUrdf(robotName + "_" + partName + ".urdf", saveVisuals)