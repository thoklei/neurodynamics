from manim import *
import numpy as np 

class FixedPoints(Scene):

    def construct(self):
        numberplane = NumberPlane()
        self.play(
            Create(numberplane)
        )
        self.wait()

        def draw_curve(func, color):
            self.curve = VGroup()
            x = -3 * PI
            curve_start = np.array([x,0,0])
            self.curve.add(Line(curve_start,curve_start))
            delta = 0.1

            while(x < 3 * PI):
                last_line = self.curve[-1]
                x += delta
                y = func(x)
                new_line = Line(last_line.get_end(),np.array([x,y,0]), color=color)
                self.curve.add(new_line)

            self.play(
                Create(self.curve)
            )
            self.wait()

        def draw_dots(color):
            for i in range(-2, 3):
                x = i * PI
                d = Dot(RIGHT*x, color=color)
                self.play(
                    FadeInFromLarge(d)
                )


        func = lambda x : np.sin(x+PI)
        draw_curve(np.sin, YELLOW_D)
        draw_curve(func, BLUE_D)

        draw_dots(RED_E)

        self.wait()
