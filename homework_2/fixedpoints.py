from manim import *
import numpy as np 

class FixedPoints(Scene):

    def get_trajectory(self, start_point, time, dt=0.1, added_steps=100):
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

    def show_many_trajectories(self):
        plane = self.numberplane

        n = 20

        start_points = [
            plane.coords_to_point(x, y)
            for x in np.linspace(-8, 8, n)
            for y in np.linspace(-4, 4, n)
        ]
        start_points.sort(
            key=lambda p: np.dot(p, UL)
        )
        time = 10

        # Count points
        dots = VGroup(*[
            Dot(sp, radius=0.025)
            for sp in start_points
        ])
        dots.set_color_by_gradient(PINK, BLUE, YELLOW)
       
        self.play(
            LaggedStartMap(
                FadeInFromLarge, dots,
                lambda m: (m, 10),
                run_time=2
            )        
        )
        self.wait()

        trajs = VGroup()
        for sp in start_points:
            trajs.add(
                self.get_trajectory(
                    sp, time,
                    added_steps=10,
                )
            )
        for traj, dot in zip(trajs, dots):
            traj.set_stroke(dot.get_color(), 1)

        def update_dots(ds):
            for d, t in zip(ds, trajs):
                d.move_to(t.get_points()[-1])
            return ds
        dots.add_updater(update_dots)

        self.add(dots, trajs)
        self.play(
            ShowCreation(
                trajs,
                lag_ratio=0,
            ),
            rate_func=linear,
            run_time=time,
        )

        self.wait()

    def construct(self):
        self.numberplane = NumberPlane()
        self.play(
            Create(self.numberplane)
        )

        self.wait(11)

        # displaying some random lines that meet
        random_line1 = Line(-10*RIGHT + -8*UP, 10*RIGHT + 12*UP, color=YELLOW_D)
        random_line2 = Line(-10*RIGHT + 7*UP, 10*RIGHT + -3*UP, color=BLUE_D)
        random_dot = Dot(ORIGIN + 2*UP, color=RED_E)
        self.play(
            Create(random_line1),
            Create(random_line2),
            Create(random_dot)
        )
        self.wait(2)

        self.play(
            FadeOut(random_line1),
            FadeOut(random_line2),
            FadeOut(random_dot)
        )
        self.wait(10)

        # displaying arbitrary functions
        colors = [YELLOW_D, BLUE_D, GREEN_D]
        random_funcs = [
            lambda x: 0.1*x**3,
            lambda x: 0.2*x**2 + 2,
            lambda x: -x**4 + 2*x**2 - 3
        ]
        random_curves = [VGroup(
            Line(-8*RIGHT + UP*random_funcs[i](-8), -8*RIGHT + UP*random_funcs[i](-8), color=colors[i])
        ) for i in range(len(random_funcs))]
        
        for x in np.linspace(-7, 8, 75):
            for i in range(len(random_funcs)):

                random_curves[i].add(Line(random_curves[i][-1].get_end(), RIGHT*x + UP*random_funcs[i](x), color=colors[i]))

        for c in random_curves:
            c.make_smooth()

            self.play(
                Create(c)
            )
        self.wait() # "and all of that for a drop of blood..."
        
        for c in random_curves:
            self.play(
                FadeOut(c)
            )

        self.wait(6)

        def draw_curve(func, color):
            curve = VGroup()
            x = -3 * PI
            curve_start = np.array([x,0,0])
            curve.add(Line(curve_start,curve_start))
            delta = 0.1

            while(x < 3 * PI):
                last_line = curve[-1]
                x += delta
                y = func(x)
                new_line = Line(last_line.get_end(),np.array([x,y,0]), color=color)
                curve.add(new_line)

            self.play(
                Create(curve)
            )
            self.wait()
            return curve

        def draw_dots(color):
            dots = VGroup()
            for i in range(-2, 3):
                x = i * PI
                d = Dot(RIGHT*x, color=color)
                dots.add(d)
                self.play(
                    FadeInFromLarge(d)
                )
            return dots

        func = lambda x : np.sin(x+PI)
        curve1 = draw_curve(np.sin, YELLOW_D)
        curve2 = draw_curve(func, BLUE_D)
        dots = draw_dots(RED_E)

        self.wait(10)

        self.play(
            FadeOut(curve1),
            FadeOut(curve2),            
            FadeOut(dots),
            FadeOut(self.numberplane),
        )

        # show analytic solution backwards

        sine_formula = MathTex("\\dot{x}=","y(t)","-","sin(x(t))")
        sine_equal = MathTex("y(t)","=","sin(x(t))")
        sine_zero = MathTex("0","=","y(t) - sin(x(t))")

        shift_sine_formula = MathTex("\\dot{y}=","y(t)","-","sin(x(t) + \\pi)")
        shift_sine_equal = MathTex("y(t)","=","sin(x(t) + \\pi)")
        shift_sine_zero = MathTex("0","=","y(t) - sin(x(t) + \\pi)")

        def explain_formula(equal, zero, formula, w1, w2, w3):
            self.play(
                Write(equal),
            )
            self.wait(w1)

            self.play(
                Transform(equal, zero)
            )
            self.wait(w2)
            self.play(
                Transform(equal, formula)
            )
            self.wait(w3)
            self.play(
                FadeOut(equal)
            )
            self.wait()

        self.wait(3)
        explain_formula(sine_equal, sine_zero, sine_formula, 7, 2, 3)
        explain_formula(shift_sine_equal, shift_sine_zero, shift_sine_formula, 2, 2, 1)

        form_group = VGroup(sine_formula, shift_sine_formula).arrange(DOWN)
        self.play(
            FadeInFrom(form_group, UP)
        )
        self.wait(2)

        self.play(
            FadeOutAndShift(form_group, DOWN)
        )

        vec_field_func = lambda t: np.array([
            t[1] - np.sin(t[0]),
            t[1] - np.sin(t[0] + PI),
            0.0
        ])

        self.play(
            Create(self.numberplane)
        )

        self.vector_field = ArrowVectorField(vec_field_func)
        self.play(*[GrowArrow(vec) for vec in self.vector_field])

        self.wait(10)
        curve1 = draw_curve(np.sin, YELLOW_D)
        curve2 = draw_curve(func, BLUE_D)

        self.wait(6)
        self.play(
            FadeOut(curve1),
            FadeOut(curve2)
        )

        self.show_many_trajectories()

        self.wait(10)
        
