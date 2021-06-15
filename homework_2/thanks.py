from manim import *
import numpy as np 

class Thanks(Scene):
    
    def construct(self):

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

