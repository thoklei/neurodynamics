from manim import *
import numpy as np 

class Nullclines(Scene):
    
    def construct(self):
        # self.setup_axes()
        number_plane = NumberPlane()
        func = lambda t: np.array([
            t[0]*(2-t[0]-t[1]),
            t[1]*(-1+t[0]),
            0
        ])

        func1 = lambda t: 0
        #graph1 = number_plane.get_graph(func1 , x_min=-5, x_max=5)

        func2 = lambda t: 2 - t
        #graph2 = number_plane.get_graph(func2 , x_min=-5, x_max=5)

        # func3 = lambda t: t
        # graph3 = 
        

        vector_field = ArrowVectorField(func)
        self.add(number_plane)
        self.play(*[GrowArrow(vec) for vec in vector_field])

        self.wait(2)

        #self.play(Create(graph1), Create(graph2))