import maya.cmds as cmds
from collections import OrderedDict
from functools import partial

# Create the window
window_name = "MyWindow"
if cmds.window(window_name, exists=True):
    cmds.deleteUI(window_name)
if cmds.windowPref(window_name, exists=True):
    cmds.windowPref(window_name, remove=True)

cmds.window(window_name, title="My Window", width=300, height=200)

# Adding layout
my_layout = cmds.columnLayout("layout_id", parent=window_name)

# Create the joints dictionary
def create_joints_dictionary(joint_listNames):
    joint_dictionary = OrderedDict()
    for joint_name in joint_listNames:
        position = cmds.xform(joint_name, query=True, worldSpace=True, translation=True)
        joint_dictionary[joint_name] = position
    return joint_dictionary

joint_listNames = [
    'Character1_Hips', 'Character1_LeftUpLeg', 'Character1_RightUpLeg', 'Character1_Spine', 'Character1_LeftLeg',
    'Character1_LeftFoot', 'Character1_LeftToeBase', 'Character1_RightLeg', 'Character1_RightFoot',
    'Character1_RightToeBase', 'Character1_Spine1', 'Character1_Spine2', 'Character1_LeftShoulder',
    'Character1_LeftArm', 'Character1_LeftForeArm', 'Character1_LeftHand', 'Character1_LeftHandThumb1',
    'Character1_LeftHandThumb2', 'Character1_LeftHandThumb3', 'Character1_LeftHandThumb4',
    'Character1_LeftHandIndex1', 'Character1_LeftHandIndex2', 'Character1_LeftHandIndex3',
    'Character1_LeftHandIndex4', 'Character1_LeftHandMiddle1', 'Character1_LeftHandMiddle2',
    'Character1_LeftHandMiddle3', 'Character1_LeftHandMiddle4', 'Character1_LeftHandRing1',
    'Character1_LeftHandRing2', 'Character1_LeftHandRing3', 'Character1_LeftHandRing4',
    'Character1_LeftHandPinky1', 'Character1_LeftHandPinky2', 'Character1_LeftHandPinky3', 'Character1_LeftHandPinky4',
    'Character1_RightShoulder', 'Character1_RightArm', 'Character1_RightForeArm', 'Character1_RightHand',
    'Character1_RightHandThumb1', 'Character1_RightHandThumb2', 'Character1_RightHandThumb3',
    'Character1_RightHandThumb4', 'Character1_RightHandIndex1', 'Character1_RightHandIndex2',
    'Character1_RightHandIndex3', 'Character1_RightHandIndex4', 'Character1_RightHandMiddle1',
    'Character1_RightHandMiddle2', 'Character1_RightHandMiddle3', 'Character1_RightHandMiddle4',
    'Character1_RightHandRing1', 'Character1_RightHandRing2', 'Character1_RightHandRing3',
    'Character1_RightHandRing4', 'Character1_RightHandPinky1', 'Character1_RightHandPinky2',
    'Character1_RightHandPinky3', 'Character1_RightHandPinky4', 'Character1_Neck', 'Character1_Head'
]

# Filling the dictionary
joint_dictionary = create_joints_dictionary(joint_listNames)
# Create locators with the dictionary coordinates
name_locator = ""
new_list = []
def create_locator(joint_listNames, *args):
    for i, (joint_name, position) in enumerate(joint_dictionary.items()):
        print(joint_name, position)
        name_locator = joint_listNames[i] + "_locator"
        my_locator = cmds.spaceLocator(name=name_locator)
        cmds.xform(my_locator[0], translation=position, worldSpace=True)
        new_list.append(my_locator)
new_function = create_locator
def connect_locators(new_function, *args):
    cmds.delete('Character1_Reference')
    cmds.spaceLocator(name = 'All')
    cmds.parent('Character1_Hips_locator','All')
    cmds.parent('Character1_LeftUpLeg_locator','Character1_Hips_locator')
    cmds.parent('Character1_LeftLeg_locator','Character1_LeftUpLeg_locator')
    cmds.parent('Character1_LeftFoot_locator','Character1_LeftLeg_locator')
    cmds.parent('Character1_LeftToeBase_locator','Character1_LeftFoot_locator')
    cmds.parent('Character1_RightUpLeg_locator','Character1_Hips_locator')
    cmds.parent('Character1_RightLeg_locator','Character1_RightUpLeg_locator')
    cmds.parent('Character1_RightFoot_locator','Character1_RightLeg_locator')
    cmds.parent('Character1_RightToeBase_locator','Character1_RightFoot_locator')
    cmds.parent('Character1_Spine_locator','Character1_Hips_locator')
    cmds.parent('Character1_Spine1_locator','Character1_Spine_locator')
    cmds.parent('Character1_Spine2_locator','Character1_Spine1_locator')
    cmds.parent('Character1_Neck_locator','Character1_Spine2_locator')
    cmds.parent('Character1_Head_locator','Character1_Neck_locator')
   
    cmds.parent('Character1_LeftShoulder_locator','Character1_Spine2_locator')
    cmds.parent('Character1_LeftArm_locator','Character1_LeftShoulder_locator')
    cmds.parent('Character1_LeftForeArm_locator','Character1_LeftArm_locator')
    cmds.parent('Character1_LeftHand_locator','Character1_LeftForeArm_locator')
    cmds.parent('Character1_LeftHandThumb1_locator','Character1_LeftHand_locator')
    cmds.parent('Character1_LeftHandThumb2_locator','Character1_LeftHandThumb1_locator')
    cmds.parent('Character1_LeftHandThumb3_locator','Character1_LeftHandThumb2_locator')
    cmds.parent('Character1_LeftHandThumb4_locator','Character1_LeftHandThumb3_locator')
    cmds.parent('Character1_LeftHandIndex1_locator','Character1_LeftHand_locator')
    cmds.parent('Character1_LeftHandIndex2_locator','Character1_LeftHandIndex1_locator')
    cmds.parent('Character1_LeftHandIndex3_locator','Character1_LeftHandIndex2_locator')
    cmds.parent('Character1_LeftHandIndex4_locator','Character1_LeftHandIndex3_locator')
    cmds.parent('Character1_LeftHandMiddle1_locator','Character1_LeftHand_locator')
    cmds.parent('Character1_LeftHandMiddle2_locator','Character1_LeftHandMiddle1_locator')
    cmds.parent('Character1_LeftHandMiddle3_locator','Character1_LeftHandMiddle2_locator')
    cmds.parent('Character1_LeftHandMiddle4_locator','Character1_LeftHandMiddle3_locator')
    cmds.parent('Character1_LeftHandRing1_locator','Character1_LeftHand_locator')
    cmds.parent('Character1_LeftHandRing2_locator','Character1_LeftHandRing1_locator')
    cmds.parent('Character1_LeftHandRing3_locator','Character1_LeftHandRing2_locator')
    cmds.parent('Character1_LeftHandRing4_locator','Character1_LeftHandRing3_locator')
    cmds.parent('Character1_LeftHandPinky1_locator','Character1_LeftHand_locator')
    cmds.parent('Character1_LeftHandPinky2_locator','Character1_LeftHandPinky1_locator')
    cmds.parent('Character1_LeftHandPinky3_locator','Character1_LeftHandPinky2_locator')
    cmds.parent('Character1_LeftHandPinky4_locator','Character1_LeftHandPinky3_locator')
   
    cmds.parent('Character1_RightShoulder_locator','Character1_Spine2_locator')
    cmds.parent('Character1_RightArm_locator','Character1_RightShoulder_locator')
    cmds.parent('Character1_RightForeArm_locator','Character1_RightArm_locator')
    cmds.parent('Character1_RightHand_locator','Character1_RightForeArm_locator')
    cmds.parent('Character1_RightHandThumb1_locator','Character1_RightHand_locator')
    cmds.parent('Character1_RightHandThumb2_locator','Character1_RightHandThumb1_locator')
    cmds.parent('Character1_RightHandThumb3_locator','Character1_RightHandThumb2_locator')
    cmds.parent('Character1_RightHandThumb4_locator','Character1_RightHandThumb3_locator')
    cmds.parent('Character1_RightHandIndex1_locator','Character1_RightHand_locator')
    cmds.parent('Character1_RightHandIndex2_locator','Character1_RightHandIndex1_locator')
    cmds.parent('Character1_RightHandIndex3_locator','Character1_RightHandIndex2_locator')
    cmds.parent('Character1_RightHandIndex4_locator','Character1_RightHandIndex3_locator')
    cmds.parent('Character1_RightHandMiddle1_locator','Character1_RightHand_locator')
    cmds.parent('Character1_RightHandMiddle2_locator','Character1_RightHandMiddle1_locator')
    cmds.parent('Character1_RightHandMiddle3_locator','Character1_RightHandMiddle2_locator')
    cmds.parent('Character1_RightHandMiddle4_locator','Character1_RightHandMiddle3_locator')
    cmds.parent('Character1_RightHandRing1_locator','Character1_RightHand_locator')
    cmds.parent('Character1_RightHandRing2_locator','Character1_RightHandRing1_locator')
    cmds.parent('Character1_RightHandRing3_locator','Character1_RightHandRing2_locator')
    cmds.parent('Character1_RightHandRing4_locator','Character1_RightHandRing3_locator')
    cmds.parent('Character1_RightHandPinky1_locator','Character1_RightHand_locator')
    cmds.parent('Character1_RightHandPinky2_locator','Character1_RightHandPinky1_locator')
    cmds.parent('Character1_RightHandPinky3_locator','Character1_RightHandPinky2_locator')
    cmds.parent('Character1_RightHandPinky4_locator','Character1_RightHandPinky3_locator')
hierarchy_locators = partial(connect_locators, new_function)

#creating joints
def create_real_joints(*args):
    t = 0
    main_joint = cmds.createNode('joint', name = "Main")
    joints_list = []
    for i in new_list:
        first_half = new_list[t][0].split("_locator")[0]
        joint_name = first_half + "_jnt"
        joints = cmds.createNode('joint', name = joint_name)
        parent_constraint_name = cmds.parentConstraint(new_list[t], joints, maintainOffset = False)
        t+=1
        cmds.delete(parent_constraint_name)   
        joints_list.append(joints)     
new_function1 = create_real_joints

#creating hierarchy of joints
def hierarchy_joints(*args):
    
    cmds.parent('Character1_LeftUpLeg_jnt','Character1_Hips_jnt')
    cmds.parent('Character1_LeftLeg_jnt','Character1_LeftUpLeg_jnt')
    cmds.parent('Character1_LeftFoot_jnt','Character1_LeftLeg_jnt')
    cmds.parent('Character1_LeftToeBase_jnt','Character1_LeftFoot_jnt')
    cmds.parent('Character1_RightUpLeg_jnt','Character1_Hips_jnt')
    cmds.parent('Character1_RightLeg_jnt','Character1_RightUpLeg_jnt')
    cmds.parent('Character1_RightFoot_jnt','Character1_RightLeg_jnt')
    cmds.parent('Character1_RightToeBase_jnt','Character1_RightFoot_jnt')
    cmds.parent('Character1_Spine_jnt','Character1_Hips_jnt')
    cmds.parent('Character1_Spine1_jnt','Character1_Spine_jnt')
    cmds.parent('Character1_Spine2_jnt','Character1_Spine1_jnt')
    cmds.parent('Character1_Neck_jnt','Character1_Spine2_jnt')
    cmds.parent('Character1_Head_jnt','Character1_Neck_jnt')
   
    cmds.parent('Character1_LeftShoulder_jnt','Character1_Spine2_jnt')
    cmds.parent('Character1_LeftArm_jnt','Character1_LeftShoulder_jnt')
    cmds.parent('Character1_LeftForeArm_jnt','Character1_LeftArm_jnt')
    cmds.parent('Character1_LeftHand_jnt','Character1_LeftForeArm_jnt')
    cmds.parent('Character1_LeftHandThumb1_jnt','Character1_LeftHand_jnt')
    cmds.parent('Character1_LeftHandThumb2_jnt','Character1_LeftHandThumb1_jnt')
    cmds.parent('Character1_LeftHandThumb3_jnt','Character1_LeftHandThumb2_jnt')
    cmds.parent('Character1_LeftHandThumb4_jnt','Character1_LeftHandThumb3_jnt')
    cmds.parent('Character1_LeftHandIndex1_jnt','Character1_LeftHand_jnt')
    cmds.parent('Character1_LeftHandIndex2_jnt','Character1_LeftHandIndex1_jnt')
    cmds.parent('Character1_LeftHandIndex3_jnt','Character1_LeftHandIndex2_jnt')
    cmds.parent('Character1_LeftHandIndex4_jnt','Character1_LeftHandIndex3_jnt')
    cmds.parent('Character1_LeftHandMiddle1_jnt','Character1_LeftHand_jnt')
    cmds.parent('Character1_LeftHandMiddle2_jnt','Character1_LeftHandMiddle1_jnt')
    cmds.parent('Character1_LeftHandMiddle3_jnt','Character1_LeftHandMiddle2_jnt')
    cmds.parent('Character1_LeftHandMiddle4_jnt','Character1_LeftHandMiddle3_jnt')
    cmds.parent('Character1_LeftHandRing1_jnt','Character1_LeftHand_jnt')
    cmds.parent('Character1_LeftHandRing2_jnt','Character1_LeftHandRing1_jnt')
    cmds.parent('Character1_LeftHandRing3_jnt','Character1_LeftHandRing2_jnt')
    cmds.parent('Character1_LeftHandRing4_jnt','Character1_LeftHandRing3_jnt')
    cmds.parent('Character1_LeftHandPinky1_jnt','Character1_LeftHand_jnt')
    cmds.parent('Character1_LeftHandPinky2_jnt','Character1_LeftHandPinky1_jnt')
    cmds.parent('Character1_LeftHandPinky3_jnt','Character1_LeftHandPinky2_jnt')
    cmds.parent('Character1_LeftHandPinky4_jnt','Character1_LeftHandPinky3_jnt')
   
    cmds.parent('Character1_RightShoulder_jnt','Character1_Spine2_jnt')
    cmds.parent('Character1_RightArm_jnt','Character1_RightShoulder_jnt')
    cmds.parent('Character1_RightForeArm_jnt','Character1_RightArm_jnt')
    cmds.parent('Character1_RightHand_jnt','Character1_RightForeArm_jnt')
    cmds.parent('Character1_RightHandThumb1_jnt','Character1_RightHand_jnt')
    cmds.parent('Character1_RightHandThumb2_jnt','Character1_RightHandThumb1_jnt')
    cmds.parent('Character1_RightHandThumb3_jnt','Character1_RightHandThumb2_jnt')
    cmds.parent('Character1_RightHandThumb4_jnt','Character1_RightHandThumb3_jnt')
    cmds.parent('Character1_RightHandIndex1_jnt','Character1_RightHand_jnt')
    cmds.parent('Character1_RightHandIndex2_jnt','Character1_RightHandIndex1_jnt')
    cmds.parent('Character1_RightHandIndex3_jnt','Character1_RightHandIndex2_jnt')
    cmds.parent('Character1_RightHandIndex4_jnt','Character1_RightHandIndex3_jnt')
    cmds.parent('Character1_RightHandMiddle1_jnt','Character1_RightHand_jnt')
    cmds.parent('Character1_RightHandMiddle2_jnt','Character1_RightHandMiddle1_jnt')
    cmds.parent('Character1_RightHandMiddle3_jnt','Character1_RightHandMiddle2_jnt')
    cmds.parent('Character1_RightHandMiddle4_jnt','Character1_RightHandMiddle3_jnt')
    cmds.parent('Character1_RightHandRing1_jnt','Character1_RightHand_jnt')
    cmds.parent('Character1_RightHandRing2_jnt','Character1_RightHandRing1_jnt')
    cmds.parent('Character1_RightHandRing3_jnt','Character1_RightHandRing2_jnt')
    cmds.parent('Character1_RightHandRing4_jnt','Character1_RightHandRing3_jnt')
    cmds.parent('Character1_RightHandPinky1_jnt','Character1_RightHand_jnt')
    cmds.parent('Character1_RightHandPinky2_jnt','Character1_RightHandPinky1_jnt')
    cmds.parent('Character1_RightHandPinky3_jnt','Character1_RightHandPinky2_jnt')
    cmds.parent('Character1_RightHandPinky4_jnt','Character1_RightHandPinky3_jnt')

#create controls 
def controls(*args, joint_list):
    n = 0
    for i in joint_list:
        control = cmds.circle(name = "control1", radius = 3, normal = (0, 1, 0))
        cmds.parentConstraint(control, joint_list[n])
        n += 1
    
btn_command = partial(create_locator, joint_listNames)
btn1 = cmds.button(label = "Create locators", parent = my_layout, command = btn_command, width = 150)
btn2 = cmds.button(label="Create hierarchy", parent=my_layout, command=hierarchy_locators, width = 150)
btn3 = cmds.button(label = "Create joints", parent = my_layout, command = new_function1, width = 150)
btn4 = cmds.button(label = "Create jnt hierarchy", parent = my_layout, command = hierarchy_joints, width = 150)
btn5 = cmds.button(label = "Create controls", parent = my_layout, command = controls, width = 150)
cmds.showWindow(window_name)