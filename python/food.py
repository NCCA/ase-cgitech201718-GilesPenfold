##################################################################################
# Giles Penfold - s5005745 Genetic Flocking Simulation, MSc CAVE ASE 2017/8
# Derived from the YABI implementation of flocking and processing.org
# Base layout from the NGL library Python example
####################### IMPORTS ##################################################
import numpy as np
import random
from pyngl import *
###################### END IMPORTS ###############################################

###
# FOOD
# Controls the food in the scene
###
class Food():

    def __init__(self, *args, **kwargs):
        self.m_pos = kwargs.get('_pos', np.random.uniform(-25, 25, 2))
        self.m_stock = kwargs.get('_stock', random.randint(25,50))

    ###
    # RESET
    # Resets a piece of food to a new position and value
    ###
    def Reset(self):
        self.m_pos = np.random.uniform(-25, 25, 2)
        self.m_stock = random.randint(25,50)
    ###
    # DRAW
    # Draws the food in the scene
    ###
    def Draw(self, _camera):
        shader = ShaderLib.instance()

        t = Transformation()
        t.setScale(self.m_stock*0.05,self.m_stock*0.05,self.m_stock*0.05)
        t.setPosition(self.m_pos[0], self.m_pos[1], 0)

        M = t.getMatrix()
        MV = _camera.getViewMatrix()*M
        MVP = _camera.getVPMatrix()*M

        shader.setUniform("MVP", MVP)

        prim = VAOPrimitives.instance()
        prim.draw("disc")
