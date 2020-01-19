import Sofa
import sys    
import random

class timing(Sofa.PythonScriptController):
    
    # optionnally, script can create a graph...
    def initGraph(self,node):
        self.nodeLiver = node.getChild('Liver')
        self.activeRandomize=1
        self.time = 0

        self.nodeLiver.getObject('CFF').findData("forces").value = "0 0 0 "

        #save a pointer to the ConstantForceField
        self.RandomForce = self.nodeLiver.getObject('CFF')
        return 0

    def bwdInitGraph(self,node):
        #count the number of points
        self.nbPoints = self.nodeLiver.getObject('dofs').findData("size").value
        print "nbPoints = "+str(self.nbPoints)
        return 0

    def onBeginAnimationStep(self,dt):
        self.time += dt
        if self.time > 10.:
            # self.constant_force_field.findData('force').value = "0 5000 0"
            self.nodeLiver.getObject('CFF').findData("forces").value = "10 0 0 "
        # print "time = "+str(self.time)

        # if self.activeRandomize==1 :
        #     newIndice = random.randint(1,self.nbPoints)
        #     self.nodeLiver.getObject('CFF').findData("indices").value = newIndice
        #     print "Randomizing force on point = "+str(newIndice)
        return 0

    # def onKeyPressed(self, c):
    #     if c=="L" :
    #         if self.activeRandomize==1 :
    #             self.activeRandomize=0
    #             print "Randomizing inactive"
    #         else:
    #             self.activeRandomize=1
    #             print "Randomizing active"
    #     return 0;