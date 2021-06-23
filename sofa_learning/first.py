import Sofa.Core

# Required import for python
import Sofa


# Choose in your script to activate or not the GUI
USE_GUI = True


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
        totalMass = 1.0
        volume = 1.0
        inertiaMatrix = [1., 0., 0., 0., 1., 0., 0., 0., 1.]
        rootNode.addObject("OglGrid", nbSubdiv=10, size=1000)
        rootNode.findData('gravity').value = [0.0, -981.0, 0.0];
        rootNode.findData('dt').value = 0.01
        # 添加子节点用于配置 scen
        confignode = rootNode.addChild("Config")
        confignode.addObject('RequiredPlugin', name="SofaMiscCollision", printLog=False)
        confignode.addObject('RequiredPlugin', name="SofaPython3", printLog=False)
        confignode.addObject('OglSceneFrame', style="Arrows", alignment="TopRight")

        # Creating the sphere
        sphere = rootNode.addChild("sphere")
        sphere.addObject('MechanicalObject', name="mstate", template="Rigid3", translation2=[0., 0., 0.],
                         rotation2=[0., 0., 0.], showObjectScale=50)
        #### visualization
        sphereVisu = sphere.addChild("VisualModel")
        sphereVisu.loader = sphereVisu.addObject('MeshObjLoader', name="loader", filename="mesh/ball.obj")
        sphereVisu.addObject('OglModel', name="model", src="@loader", scale3d=[50] * 3, color=[0., 1., 0.],
                             updateNormals=False)
        sphereVisu.addObject('RigidMapping')

        # 属性给sphere
        sphere.addObject('UniformMass', name="mass", vertexMass=[totalMass, volume, inertiaMatrix[:]])
        sphere.addObject('UncoupledConstraintCorrection') # 计算球的约束力
        # 用两个不同的求解器
        # 时间积分方案，定义了系统在每个时间步的模拟(这里是隐式欧拉方法）
        sphere.addObject('EulerImplicitSolver', name='odesolver')
        # 共轭梯度方法(Conjugate gradient method)，在每个time step解控制模型的方程，并给 机械对象更新。
        sphere.addObject('CGLinearSolver', name='Solver')


        # 添加地板 同样的分为机械模型和视觉模型
        floor = rootNode.addChild("floor")
        floor.addObject('MechanicalObject', name="mstate", template="Rigid3", translation2=[0.0, -300.0, 0.0],
                        rotation2=[0., 0., 0.], showObjectScale=5.0)
        floor.addObject('UniformMass', name="mass", vertexMass=[totalMass, volume, inertiaMatrix[:]])

        floorVisu = floor.addChild("VisualModel")
        floorVisu.loader = floorVisu.addObject('MeshObjLoader', name="loader", filename="mesh/floor.obj")
        floorVisu.addObject('OglModel', name="model", src="@loader", scale3d=[5.0] * 3, color=[1., 1., 0.],
                            updateNormals=False)
        floorVisu.addObject('RigidMapping')


        # 碰撞建模
        # DefaultAnimationLoop
        rootNode.addObject('DefaultPipeline')
        rootNode.addObject('FreeMotionAnimationLoop')
        rootNode.addObject('GenericConstraintSolver', tolerance="1e-6", maxIterations="1000")
        rootNode.addObject('BruteForceDetection')
        rootNode.addObject('RuleBasedContactManager', responseParams="mu=" + str(0.0), name='Response',
                           response='FrictionContact')
        rootNode.addObject('LocalMinDistance', alarmDistance=10, contactDistance=5, angleCone=0.01)


        # 给球体添加一个  负责碰撞的节点
        collision = sphere.addChild('collision')
        collision.addObject('MeshObjLoader', name="loader", filename="mesh/ball.obj", triangulate="true", scale=45.0)

        collision.addObject('MeshTopology', src="@loader")
        collision.addObject('MechanicalObject')

        collision.addObject('TriangleCollisionModel')
        collision.addObject('LineCollisionModel')
        collision.addObject('PointCollisionModel')

        collision.addObject('RigidMapping')

        # 给地板也来一个 碰撞的节点
        floorCollis = floor.addChild('collision')
        floorCollis.addObject('MeshObjLoader', name="loader", filename="mesh/floor.obj", triangulate="true", scale=5.0)
        floorCollis.addObject('MeshTopology', src="@loader")
        floorCollis.addObject('MechanicalObject')
        floorCollis.addObject('TriangleCollisionModel', moving=False, simulated=False)
        floorCollis.addObject('LineCollisionModel', moving=False, simulated=False)
        floorCollis.addObject('PointCollisionModel', moving=False, simulated=False)

        floorCollis.addObject('RigidMapping')

        return rootNode



if __name__ == '__main__':
    main()