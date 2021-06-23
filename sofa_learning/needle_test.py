import Sofa.Core

# Required import for python
import Sofa


# Choose in your script to activate or not the GUI
USE_GUI = True
# from stlib.physics.rigid import Floor

def main():
    import SofaRuntime
    import Sofa.Gui
    SofaRuntime.importPlugin("SofaOpenglVisual")
    SofaRuntime.importPlugin("SofaImplicitOdeSolver")

    root = Sofa.Core.Node("root")
    createScene(root)
    Sofa.Simulation.init(root)

    if not USE_GUI:
        for iteration in range(10):
            Sofa.Simulation.animate(root, root.dt.value)
    else:
        Sofa.Gui.GUIManager.Init("myscene", "qglviewer")
        Sofa.Gui.GUIManager.createGUI(root, __file__)
        Sofa.Gui.GUIManager.SetDimension(1080, 1080)
        Sofa.Gui.GUIManager.MainLoop(root)
        Sofa.Gui.GUIManager.closeGUI()
def createScene(rootNode):
    dt = 0.02  # In second
    displayFlags = ['showForceFields', 'showCollisionModels', 'showBehavior']

    rootNode.addObject("OglGrid", nbSubdiv=10, size=1000)
    rootNode.findData('gravity').value = [0, 0, 0]
    rootNode.findData('dt').value = dt

    rootNode.addObject('RequiredPlugin', name='SofaMiscCollision')
    rootNode.addObject('RequiredPlugin', name='SofaPython3')
    rootNode.addObject('RequiredPlugin', name='CImgPlugin')
    rootNode.addObject('RequiredPlugin', name='SofaOpenglVisual')

    rootNode.addObject('VisualStyle', displayFlags=displayFlags)
    rootNode.addObject('FreeMotionAnimationLoop')

    rootNode.addObject('GenericConstraintSolver', maxIterations=1000, tolerance=1e-07)
    rootNode.addObject('DefaultPipeline', verbose='0', depth="6", draw='1')
    rootNode.addObject('BruteForceDetection', name='N2')
    # self.rootNode.createObject('DiscreteIntersection', name='Intersection')
    rootNode.addObject("LocalMinDistance", name="Intersection", alarmDistance="0.3", contactDistance="0.1",
                               useLMDFilters="0")
    rootNode.addObject('DefaultContactManager', name="Response", response="FrictionContact",
                               responseParams='mu=0.8')

    # ==========================
    # NEEDLE NODE
    # ==========================

    meshFile = "needle.obj"
    scale = 10
    needleNode = rootNode.addChild("Needle")

    needleNode.addObject('EulerImplicitSolver', name="ODE solver", rayleighStiffness="0.01", rayleighMass="1.0")
    needleNode.addObject('CGLinearSolver', name="linear solver", iterations="25", tolerance="1e-10",
                            threshold="10e-10")
    needleNode.addObject('MechanicalObject', name="mechObject", template="Rigid3d", dx=0, dy=150, dz=-50, rx=0,
                            ry=0, rz=-90.0, scale3d=[scale, scale, scale])
    needleNode.addObject('UniformMass', name="mass", totalMass="5")
    needleNode.addObject('UncoupledConstraintCorrection')

    # Visual node
    needleVisNode = needleNode.addChild("VisualModel")
    needleVisNode.addObject('MeshObjLoader', name='instrumentMeshLoader', filename=meshFile)
    needleVisNode.addObject('OglModel', name="InstrumentVisualModel", src='@instrumentMeshLoader', dy=-2 * scale,
                               scale3d=[scale, scale, scale])
    needleVisNode.addObject('RigidMapping', name="MM-VM mapping", input="@../mechObject",
                               output="@InstrumentVisualModel")
    # Collision node
    needleColNode = needleNode.addChild("CollisionModel")
    needleColNode.addObject('MeshObjLoader', filename=meshFile, name="loader")
    needleColNode.addObject('MeshTopology', src="@loader", name="InstrumentCollisionModel")
    needleColNode.addObject('MechanicalObject', src="@InstrumentCollisionModel", name="instrumentCollisionState",
                               dy=-2 * scale, scale3d=[scale, scale, scale])
    needleColNode.addObject('TriangleCollisionModel', name="instrumentTrinagle", contactStiffness="500",
                               contactFriction="0.01")
    needleColNode.addObject('LineCollisionModel', name="instrumentLine", contactStiffness="500",
                               contactFriction="0.01")
    needleColNode.addObject('PointCollisionModel', name="instrumentPoint",
                               contactStiffness="500", contactFriction="0.01")
    needleColNode.addObject('RigidMapping', name="MM-CM mapping", input="@../mechObject",
                               output="@instrumentCollisionState")

    needleNode.addObject('LinearMovementConstraint', template="Rigid3d",
                            indices=0,
                            keyTimes=[0, 0.8, 1.6, 1.7],
                            movements=[[0, 0, 0, 0, 0, 0],
                                       [0, -80, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0]])
    # Instantiate floor
    #floor = Floor(rootNode, name="Floor", translation=[0.0, -180.0, -50.0], uniformScale=6,
    #              isAStaticObject=True, color=[0.3, 0.3, 0.4])

    # ==========================
    # FAT NODE
    # ==========================

    meshFile = "tissue.stl"

    fatNode = rootNode.addChild("Fat")

    fatNode.addObject('EulerImplicitSolver', rayleighStiffness=0.1, rayleighMass=0.1)
    fatNode.addObject('CGLinearSolver', iterations=25, tolerance=1e-9, threshold=1e-9, printLog=True)
    fatNode.addObject('MechanicalObject', name='mechObject', template="Vec3d", dx="0", dy="0", dz="0", rx="0",
                         ry="0", rz="0", scale="1.0")
    fatNode.addObject('UniformMass', template="Vec3d,double", name='mass', totalMass="1")

    fatNode.addObject('RegularGridTopology', nx=10, ny=10, nz=10, xmin=-155, xmax=125, ymin=-170, ymax=45,
                         zmin=-120, zmax=10)
    # fatNode.createObject('RegularGridSpringForceField', name="Springs", stiffness="50", damping="1")
    # fatNode.createObject('HexahedronFEMForceField', template="Vec3d", name="FEM", poissonRatio="0.45", youngModulus="2000")
    fatNode.addObject('TetrahedronFEMForceField', template='Vec3d', name='FEM_tissue',
                         method='polar', poissonRatio='0.495', youngModulus='200', computeVonMisesStress='1',
                         showVonMisesStressPerNode='false', listening='1', updateStiffness='true',
                         showStressColorMap='blue 1 0 0 1  1 0.5 0.5 1', isToPrint='1')
    fatNode.addObject('UncoupledConstraintCorrection')

    # Visual node
    fatVisNode = fatNode.addChild('Visual')
    fatVisNode.addObject('MeshSTLLoader', name='meshLoader', filename=meshFile)
    fatVisNode.addObject('OglModel', src='@meshLoader', color="#ecc854", name="Fat")
    fatVisNode.addObject('BarycentricMapping', name="Visual Mapping", output="@Fat")

    # Collision node
    fatColNode = fatNode.addChild('Collision')
    fatColNode.addObject('MeshSTLLoader', name="meshLoader", filename=meshFile)
    # fatColNode.createObject('OglModel',name='Visual', src='@meshLoader', color="#ecc854")
    fatColNode.addObject('MeshTopology', src="@meshLoader")
    fatColNode.addObject('MechanicalObject', src="@meshLoader", name="CollisionObject", template="Vec3d",
                            scale="1.0")
    fatColNode.addObject('TriangleCollisionModel', template="Vec3d")
    fatColNode.addObject('LineCollisionModel')
    fatColNode.addObject('PointCollisionModel')
    fatColNode.addObject('BarycentricMapping', name="Mechanical Mapping")

    return rootNode

if __name__ == '__main__':
    main()