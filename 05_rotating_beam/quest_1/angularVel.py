import Sofa
import sys    

class rotate(Sofa.PythonScriptController):
     
    # optionnally, script can create a graph...
    def initGraph(self,node):
        nodeParticle = node.getChild('ParticleControl')
        self.engine = nodeParticle.getObject('engine')
        return 0

    def onBeginAnimationStep(self,dt):
        # adding at each time step a rotation angle in x (Euler angle) of 5 degree
        rotation = self.engine.findData('rotation').value
        rotation[0][0] = rotation[0][0] + 5
        print rotation[0][0]
        self.engine.findData('rotation').value = rotation
        return 0