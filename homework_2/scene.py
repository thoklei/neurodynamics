from manim import *
import numpy as np 

class Nullclines(Scene):

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
        plane = self.number_plane

        delta_x = 0.5
        delta_y = 0.5
        n = 10

        start_points = [
            plane.coords_to_point(x, y)
            for x in np.linspace(-8, 8, n)
            for y in np.linspace(-4, 4, n)
        ]
        start_points.sort(
            key=lambda p: np.dot(p, UL)
        )
        time = 15

        # Count points
        dots = VGroup(*[
            Dot(sp, radius=0.025)
            for sp in start_points
        ])
        dots.set_color_by_gradient(PINK, BLUE, YELLOW)
       
        self.play(
            # ShowIncreasingSubsets(dots, run_time=2),
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
            #LaggedStart(Uncreate(trajs, lag_ratio=0)),
            rate_func=linear,
            run_time=time,
        )

        self.wait()

        #self.remove(trajs)

    
    def construct(self):

        self.number_plane = NumberPlane()
        func = lambda t: np.array([
            t[0]*(2.0-t[0]-t[1]),
            t[1]*(-1.0+t[0]),
            0.0
        ])

        
        # create number plane
        self.play(
            Create(self.number_plane)
        )
        self.wait(5)

        # create vector vield
        self.vector_field = ArrowVectorField(func)
        self.play(*[GrowArrow(vec) for vec in self.vector_field])

        self.wait(3)

        self.show_many_trajectories()

        self.wait(4)


        # visualize x-Nullclines 
        xline1 = Line(5 * UP, 5 * DOWN, color="red")
        xline2 = Line(LEFT * 8 + 10 * UP, RIGHT * 8 + 6 * DOWN, color="red")
        self.play(
            Create(xline1), 
            Create(xline2)
        )
        self.wait()

        # visualize y-Nullclines 
        yline1 = Line(RIGHT + 5 * UP, RIGHT + 5 * DOWN, color="green")
        yline2 = Line(LEFT * 8, RIGHT * 8, color="green")
        self.play(
            Create(yline1), 
            Create(yline2)
        )
        self.wait()

        

        # visualize fixed points
        d1 = Dot(RIGHT + UP, color="blue")
        d2 = Dot(2*RIGHT, color="blue")
        d3 = Dot(ORIGIN, color="blue")

        self.play(
            Create(d1),
            Create(d2),
            Create(d3)
        )

        self.wait(20)
