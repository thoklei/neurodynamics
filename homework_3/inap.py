from manim import *
import numpy as np 

#config.frame_height = 0.7
#config.frame_width = 100


class Inap(Scene):


    def show_vec_field(self, func, wait):
        self.vector_field = ArrowVectorField(func,
            x_min=-8, x_max=8, 
            y_min=-7, y_max=7)
            # delta_x=5, delta_y=3
        
        self.play(*[GrowArrow(vec) for vec in self.vector_field])

        self.wait(wait)

        self.play(
            FadeOut(self.vector_field)
        )
  
    
    def construct(self):
        

        def inap_func(t):

            V = t[0] * 10.0
            n = t[1] / 10.0

            print("Calling inap at V=",V, " and n=",n)

            # parameters
            I = 0
            EL = -80
            gL = 8
            gNa = 20
            gK = 10
            V12_m = -20
            k_m = 15
            V12_n = -25
            k_n = 5
            ENa = 60
            EK = -90

            # # calculating m_inf
            m_inf = 1.0 / ( 1 + np.exp( (V12_m - V)/k_m ) )

            # # calculating tau
            tau = 1 # not sure if this is correct...

            # # calculating n_inf
            n_inf = 1.0 / ( 1.0 + np.exp( (V12_n - V)/k_n) )

            V = I - gL*( V - EL) - gNa * m_inf * (V - ENa) - gK * n*(V-EK)
            n = (n_inf - n) / tau

            # scaling
            V = V * 10.0
            n = n * 10.0

            return np.array([V, n, 0])


        self.show_vec_field(inap_func, 5)
        

        


