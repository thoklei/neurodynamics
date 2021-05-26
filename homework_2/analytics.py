from manim import *
import numpy as np 

class Analytics(Scene):
    
    def construct(self):

        # show title and initial differential equations

        title = Tex("System of differential equations:")

        self.wait()

        x_formula = MathTex(
            "\\dot{x}=","x(t)(2-x(t)-y(t))"
        )
        x_zero = MathTex(
            "0=","x(t)","(2-x(t)-y(t))"
        )

        y_formula = MathTex(
            "\\dot{y}=","y(t)(-1+x(t))"
        )
        y_zero = MathTex(
            "0=","y(t)", "(-1+x(t))"
        )

        self.play(
            Write(title),
        )
        self.wait()
        x_formula.shift(DOWN)
        y_formula.shift(DOWN * 2)
        self.play(
            LaggedStart(FadeInFrom(x_formula, DOWN)),
            LaggedStart(FadeInFrom(y_formula, DOWN))
        )
        self.wait(25)

        transform_title = Tex("Analytic Solution:")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(FadeOutAndShift(y_formula, direction=DOWN)),
        )

        self.wait(5)
        
        # explain how first diff eq can be zero

        def display_analytic_solutions(formula, zero, sol_tex1, sol_tex2, w1, w2, w3):
            framebox1 = SurroundingRectangle(zero[1], buff = .1)
            framebox2 = SurroundingRectangle(zero[2], buff = .1)
            sol1 = MathTex(sol_tex1)
            sol1.shift(DOWN)
            sol2 = MathTex(sol_tex2)
            sol2.shift(DOWN * 2)

            self.play(
                Transform(formula, zero)
            )
            self.wait(w1)

            self.play(
                Create(framebox1),
                LaggedStart(Write(sol1))
            )
            self.wait(w2)

            self.play(
                ReplacementTransform(framebox1,framebox2),
                LaggedStart(Write(sol2))
            )
            self.wait(w3)

            # clear screen
            self.play(
                FadeOut(sol1),
                FadeOut(sol2),
                FadeOut(zero),
                FadeOut(formula),
                FadeOut(framebox1),
                FadeOut(framebox2)
            )
        
        display_analytic_solutions(x_formula, x_zero, "x(t) = 0", "y(t) = 2 - x(t)", 10, 10, 25)
        self.wait()
        y_formula.shift(UP)
        self.play(
            FadeInFrom(y_formula, DOWN)
        )
        self.wait(2)
        display_analytic_solutions(y_formula, y_zero, "y(t) = 0", "x(t) = 1", 5, 3, 5)
        self.play(FadeOut(title), FadeOut(transform_title))


        # explain how second formula can be zero

class FixedPointsAnalytics(Scene):
    
    def construct(self):
        title = Tex("Calculation of fixed points")
        x_subtitle = Tex("x-nullclines:")
        y_subtitle = Tex("y-nullclines:")

        x_nullcline1 = MathTex(
            "y(t)", " = ", "2 - x(t)"
        )
 
        x_nullcline2 = MathTex(
            "x(t)", " = ", "0"
        )

        y_nullcline1 = MathTex(
            "y(t)", " = ", "0"
        )

        y_nullcline2 = MathTex(
            "x(t)", " = ", "1"
        )

        self.play(Write(title))

        self.wait(5)

        transform_title = Tex("Fixed points:")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title)
        )

        x_subtitle.shift(2*UP + 3*LEFT)
        y_subtitle.shift(2*UP + 3*RIGHT)

        x_nullcline1.shift(1*UP + 3*LEFT)
        x_nullcline2.shift(0*DOWN + 3*LEFT)
        y_nullcline1.shift(1*UP + 3*RIGHT)
        y_nullcline2.shift(0*DOWN + 3*RIGHT)

        self.play(
            LaggedStart(FadeInFrom(x_subtitle, DOWN)),
            LaggedStart(FadeInFrom(y_subtitle, DOWN))
        )

        self.wait()

        self.play(
            FadeInFrom(x_nullcline1, LEFT),
            FadeInFrom(x_nullcline2, LEFT),
            FadeInFrom(y_nullcline1, RIGHT),
            FadeInFrom(y_nullcline2, RIGHT)
        )

        framebox1 = SurroundingRectangle(x_nullcline1, buff = .1)
        framebox2 = SurroundingRectangle(x_nullcline2, buff = .1)
        framebox3 = SurroundingRectangle(y_nullcline1, buff = .1)
        framebox4 = SurroundingRectangle(y_nullcline2, buff = .1)

        self.wait(2)

        self.play(
            Create(framebox1)
        )

        self.wait()

        self.play(
            LaggedStart(Create(framebox3)),
            LaggedStart(Create(framebox4))
        )

        self.wait(2)

        self.play(
            FadeOut(framebox1),
            FadeOut(framebox3),
            FadeOut(framebox4)
        )

        self.wait()

        self.play(
            Create(framebox2)
        )

        self.wait()

        self.play(
            LaggedStart(Create(framebox3)),
            LaggedStart(Create(framebox4))
        )

        self.wait(2)

        self.play(
            FadeOut(framebox2),
            FadeOut(framebox3),
            FadeOut(framebox4)
        )

        self.wait()

        self.play(
            FadeOut(x_subtitle),
            FadeOut(y_subtitle),
            FadeOut(x_nullcline1),
            FadeOut(x_nullcline2),
            FadeOut(y_nullcline1),
            FadeOut(y_nullcline2),
        )

        self.wait()
        self.fixed_point1()

        self.wait(2)
        self.fixed_point2()

        self.wait(2)
        self.fixed_point3()

        self.wait(2)


    def fixed_point1(self):
        fixed_point1_x1 = MathTex(
            "y(t)", " = ", "2 - x(t)"
        )
        fixed_point1_x1.shift(3*LEFT)

        fixed_point1_y1 = MathTex(
            "y(t)", " = ", "0"
        )
        fixed_point1_y1.shift(3*RIGHT)

        fixed_point1_x2 = MathTex(
            "0", " = ", "2 - x(t)"
        )
        fixed_point1_x2.shift(3*LEFT)

        zero_copy = fixed_point1_y1[2].copy()

        self.play(
            FadeIn(fixed_point1_x1),
            FadeIn(fixed_point1_y1)
        )

        self.wait(2)

        self.play(
            Transform(fixed_point1_x1, fixed_point1_x2),
            Transform(zero_copy, fixed_point1_x2[0])
        )

        self.wait(3)

        fixed_point1_x3 = MathTex(
            "x(t)", "=", "2"
        )
        fixed_point1_x3.shift(3*LEFT)

        fixed_point1_y2 = MathTex(
            "y(", "2" , ")=", "0"
        )
        fixed_point1_y2.shift(3*RIGHT)

        two_copy = fixed_point1_x3[2].copy()

        self.play(
            FadeOut(fixed_point1_x1),
            FadeOut(zero_copy),
            Transform(fixed_point1_x2, fixed_point1_x3)
        )

        self.wait(2)

        self.play(
            Transform(fixed_point1_y1, fixed_point1_y2),
            Transform(two_copy, fixed_point1_y2[1])
        )
        
        self.wait(4)

        fixed_point1 = MathTex(
            "(", "2", ",", "0", ")",
            color=BLUE
        )
        fixed_point1.shift(3.35*UP + 1*LEFT)

        self.play(
            FadeIn(fixed_point1),
            Transform(fixed_point1_x3[2], fixed_point1[1]),
            Transform(fixed_point1_y2[3], fixed_point1[3])
        )
        self.wait(2)

        self.play(
            FadeOut(fixed_point1_x2),
            FadeOut(fixed_point1_y1),
            FadeOut(two_copy)
        )

    def fixed_point2(self):
        fixed_point2_x1 = MathTex(
            "y(t)", " = ", "2 - ", "x(t)"
        )
        fixed_point2_x1.shift(3*LEFT)

        # fixed_point2_x2 = MathTex(
        #     "y(t)", " = ", "2 - ", "1"
        # )
        fixed_point2_x2 = Tex(
            "y(t)", " = ", "2 - ", "1"#, tex_environment='flushleft'
        )
        fixed_point2_x2.shift(3*LEFT)

        fixed_point2_y1 = MathTex(
            "x(t)", " = ", "1"
        )
        fixed_point2_y1.shift(3*RIGHT)
        one_copy = fixed_point2_y1[2].copy()

        self.play(
            FadeIn(fixed_point2_x1),
            FadeIn(fixed_point2_y1)
        )

        self.wait()

        self.play(
            Transform(fixed_point2_x1, fixed_point2_x2),
            Transform(one_copy, fixed_point2_x2[3])
        )

        self.wait()
        
        fixed_point2_x3 = Tex(
            "y(t)", "=", "1"#, tex_environment='flushleft'
        )
        fixed_point2_x3.shift(3*LEFT)

        self.play(
            FadeOut(fixed_point2_x1),
            FadeOut(one_copy),
            Transform(fixed_point2_x2, fixed_point2_x3)
        )

        self.wait()

        fixed_point2 = MathTex(
            "(", "1", ",", "1", ")",
            color=BLUE
        )
        fixed_point2.shift(3.35*UP + 1*RIGHT)

        one_copy = fixed_point2_y1[2].copy()
        self.play(
            FadeIn(fixed_point2),
            Transform(fixed_point2_x3[2], fixed_point2[3]),
            Transform(one_copy, fixed_point2[1])
        )

        self.wait()

        self.play(
            FadeOut(fixed_point2_x2),
            FadeOut(fixed_point2_x3),
            FadeOut(fixed_point2_y1),
            FadeOut(one_copy)
        )

    def fixed_point3(self):
        fixed_point3_x1 = MathTex(
            "x(t)", " = ", "0"
        )
        fixed_point3_x1.shift(3*LEFT)

        fixed_point3_y1 = MathTex(
            "y(t)", " = ", "0"
        )
        fixed_point3_y1.shift(3*RIGHT)

        zero_copy = fixed_point3_x1[2].copy()
        one_copy = fixed_point3_y1[2].copy()

        fixed_point3 = MathTex(
            "(", "0", ",", "0", ")",
            color=BLUE
        )
        fixed_point3.shift(3.35*UP + 3*RIGHT)

        self.play(
            FadeIn(fixed_point3_x1),
            FadeIn(fixed_point3_y1)
        )

        self.wait()

        self.play(
            FadeIn(fixed_point3),
            Transform(zero_copy, fixed_point3[1]),
            Transform(one_copy, fixed_point3[3])
        )

        self.wait()

        self.play(
            FadeOut(fixed_point3_x1),
            FadeOut(fixed_point3_y1)
        )
        
    def fixed_point4(self):
        fixed_point4_x1 = MathTex(
            "x(t)", " = ", "0"
        )
        fixed_point4_x1.shift(3*LEFT)

        fixed_point4_y1 = MathTex(
            "x(t)", " = ", "1"
        )
        fixed_point4_y1.shift(3*RIGHT)

        self.play(
            FadeIn(fixed_point4_x1),
            FadeIn(fixed_point4_y1)
        )

        error = Tex("X", color=RED)

        self.wait()
        
        self.play(
            FadeIn(error)
        )

        self.wait(2)

        self.play(
            FadeOut(fixed_point4_x1),
            FadeOut(fixed_point4_y1),
            FadeOut(error)
        )