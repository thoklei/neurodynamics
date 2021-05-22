from manim import *
import numpy as np 

class Analytics(Scene):
    
    def construct(self):

        # show title and initial differential equations

        title = Tex("System of differential equations:")

        self.wait()

        x_formula = MathTex(
            "\\dot{x}=","x(t)(2-x(t)-y(t)"
        )
        x_zero = MathTex(
            "0=","x(t)","(2-x(t)-y(t)"
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
        self.wait()

        transform_title = Tex("Analytic Solution:")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(FadeOutAndShift(y_formula, direction=DOWN)),
        )

        self.wait()
        
        # explain how first diff eq can be zero

        def display_analytic_solutions(formula, zero, sol_tex1, sol_tex2):
            framebox1 = SurroundingRectangle(zero[1], buff = .1)
            framebox2 = SurroundingRectangle(zero[2], buff = .1)
            sol1 = MathTex(sol_tex1)
            sol1.shift(DOWN)
            sol2 = MathTex(sol_tex2)
            sol2.shift(DOWN * 2)

            self.play(
                Transform(formula, zero)
            )
            self.wait()

            self.play(
                Create(framebox1),
                LaggedStart(Write(sol1))
            )
            self.wait()

            self.play(
                ReplacementTransform(framebox1,framebox2),
                LaggedStart(Write(sol2))
            )
            self.wait()

            # clear screen
            self.play(
                FadeOut(sol1),
                FadeOut(sol2),
                FadeOut(zero),
                FadeOut(formula),
                FadeOut(framebox1),
                FadeOut(framebox2)
            )
        
        display_analytic_solutions(x_formula, x_zero, "x(t) = 0", "y(t) = 2 - x(t)")
        self.wait()
        y_formula.shift(UP)
        self.play(
            FadeInFrom(y_formula, DOWN)
        )
        self.wait()
        display_analytic_solutions(y_formula, y_zero, "y(t) = 0", "x(t) = 1")
        self.wait()


        # explain how second formula can be zero