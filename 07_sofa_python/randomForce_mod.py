import Sofa
import sys    
import random

class randomize(Sofa.PythonScriptController):
    
    # optionnally, script can create a graph...
    def initGraph(self,node):
        self.nodeLiver = node.getChild('Liver')
        self.activeRandomize=1

        #save a pointer to the ConstantForceField
        self.RandomForce = self.nodeLiver.getObject('CFF')
        return 0

    def bwdInitGraph(self,node):
        #count the number of points
        self.nbPoints = self.nodeLiver.getObject('dofs').findData("size").value
        print "nbPoints = "+str(self.nbPoints)
        return 0

    def onBeginAnimationStep(self,dt):
        # if active, randomly change the indice on which the force is applied
        if self.activeRandomize==1 :
            newIndice = random.randint(1,self.nbPoints)
            self.nodeLiver.getObject('CFF').findData("indices").value = newIndice
            print "Randomizing force on point = "+str(newIndice)
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