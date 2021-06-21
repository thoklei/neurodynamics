from manim import *
import numpy as np 

config.frame_height = 7
config.frame_width = 11

class Inap(Scene):

    def get_trajectory(self, start_point, time, dt=0.01, added_steps=100):
        field = self.vector_field
        traj = VMobject()
        traj.start_new_path(start_point)
        for x in range(int(time / dt)):
            last_point = traj.get_points()[-1]
            for y in range(added_steps):
                dp_dt = field.func(last_point)
                last_point += dp_dt * dt / added_steps
            traj.add_smooth_curve_to(last_point)
        #traj.make_smooth()
        traj.set_stroke(WHITE, 2)
        return traj

    def show_random_traj(self, x, y):
        start_point = x*RIGHT + y*UP #plane.coords_to_point(x,y)
        time = 40

        dot = VGroup(Dot(start_point, radius=0.025))
        dot.set_color_by_gradient(PINK, BLUE, YELLOW)

        self.play(
            LaggedStartMap(
                FadeInFromLarge, dot,
                lambda m: (m, 10),
                run_time=2
            ) 
        )
        self.wait()

        trajs = VGroup()
        trajs.add(
            self.get_trajectory(
                start_point, time,
                added_steps=10,
            )
        )
        
        trajs.set_stroke(dot.get_color(), 1)

        def update_dots(ds):
            for d, t in zip(ds, trajs):
                d.move_to(t.get_points()[-1])
            return ds
        dot.add_updater(update_dots)

        self.add(dot, trajs)
        self.play(
            ShowCreation(
                trajs,
                lag_ratio=0,
            ),
            rate_func=linear,
            run_time=time,
        )

        self.wait()

        self.play(
            FadeOut(trajs),
            FadeOut(dot)
        )

    def show_vec_field(self, func):
        self.vector_field = ArrowVectorField(func,
            x_min=-9, x_max=2, 
            y_min=0, y_max=7,
            delta_x=0.5, delta_y=0.4,
            length_func= lambda x : 0.2
            )
        
        self.play(*[GrowArrow(vec) for vec in self.vector_field])

        

    def construct(self):

        self.camera.frame_center = ORIGIN + 3.5*LEFT + 3.5 * UP
        self.camera.frame_height = 9
        self.camera.frame_width = 13
        

        def inap_func(t):

            V = t[0] * 10
            n = t[1] / 10

            # print("Calling inap at V=",V, " and n=",n)

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
            tau = 1 # using simple scenario for now

            # # calculating n_inf
            n_inf = 1.0 / ( 1.0 + np.exp( (V12_n - V)/k_n) )

            V = I - gL*( V - EL) - gNa * m_inf * (V - ENa) - gK * n*(V-EK)
            n = (n_inf - n) / tau

            # scaling
            V = V / 100
            n = n * 10.0

            # print(V, " ", n)

            return np.array([V, n, 0])


        self.show_vec_field(inap_func)

        self.show_random_traj(-5.5, 0)

        self.wait(5)

        self.play(
            FadeOut(self.vector_field)
        )


        

        


