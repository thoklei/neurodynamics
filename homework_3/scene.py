from manim import *
import numpy as np 

class RandomTrajectory(Scene):

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
        plane = self.numberplane
        start_point = plane.coords_to_point(x,y)
        time = 10

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

    def show_vec_field(self, func, wait, px, py):
        self.vector_field = ArrowVectorField(func)
        self.play(*[GrowArrow(vec) for vec in self.vector_field])

        self.wait(wait)

        self.show_random_traj(px, py)

        self.play(
            FadeOut(self.vector_field)
        )

    def thanks(self):
        title = Tex("Thank you for listening!")
        questions = Tex("Questions?")

        self.wait()

        self.play(
            Write(title),
        )
        self.wait()

        self.play(
            Transform(title, questions),
        )
        self.wait()

        self.play(
            FadeOut(title),
            FadeOut(questions)
        )

    def define(self, word, definition, focus):
        heteroclinic = Tex(word)
        hetero_def = Tex(*definition)
        hetero_def.shift(DOWN)
        framebox = SurroundingRectangle(hetero_def[focus], buff = .1)
        hetero = VGroup(heteroclinic, hetero_def)

        self.play(
            Write(heteroclinic)
        )
        self.wait()

        self.play(
            FadeInFrom(hetero_def, DOWN),
        )
        self.wait()

        self.play(
            Create(framebox)
        )

        self.play(
            FadeOut(hetero_def),
            FadeOut(heteroclinic),
            FadeOut(framebox)
        )
    
    def construct(self):

        # creating numberplane
        self.numberplane = NumberPlane()
        self.play(
            Create(self.numberplane)
        )

        self.wait(2)

        # creating vec_field
        vec_field_func = lambda t: np.array([
            t[1] - np.sin(t[0]),
            t[1] - np.sin(t[0] + PI),
            0.0
        ])

        vec_field_func2 = lambda t: np.array([
            t[0]*(2.0-t[0]-t[1]),
            t[1]*(-1.0+t[0]),
            0.0
        ])

        circular_vec_fied_func = lambda t: np.array([
            -1.0 * np.sin(PI/2.0 * t[1]),
            np.sin(PI/2.0 * t[0]),
            0
        ])


        def pendulum_vector_field_func(point, mu=0.1, g=9.8, L=3):
            theta, omega = point[:2]
            return np.array([
                omega,
                -np.sqrt(g / L) * np.sin(theta), #- mu * omega, # removing air resistance because that wouldn't work
                0,
            ])

        def pendulum_field_func(point):
            x, y = self.numberplane.point_to_coords(point)
            mu, g, L = [0.2, 4.9, 1.6]
                #big_pendulum_config[key]
                #for key in ["damping", "gravity", "length"]
            #]
            return pendulum_vector_field_func(
                x * RIGHT + y * UP,
                mu=mu, g=g, L=L
            )

        #self.show_vec_field(vec_field_func, 1, -2, 1)

        #self.show_vec_field(vec_field_func2, 1, 5, 1)

        #self.show_vec_field(circular_vec_fied_func, 5, 1, 0)

        self.show_vec_field(pendulum_field_func, 5, -PI, 0.001)

        self.play(
            FadeOut(self.numberplane)
        )

        self.define("heteroclinic", ["starts and ends in ", "different", " equilibria"], 1)
        self.define("homoclinic", ["starts and ends in ", "the same", " equilibrium"], 1)

        self.thanks()






        

        


