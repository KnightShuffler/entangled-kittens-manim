from manim import *

class Postulate1_Statement(Scene):
    def construct(self):
        title = Tex(r'\textbf{Postulate 1:}').move_to(7*LEFT+2*UP,aligned_edge=LEFT)

        statement = [
                        Tex(r'Every '),
                        Tex(r'isolated quantum system',color='yellow'),
                        Tex(r'has an associated'),
                        Tex(r"``Hilbert Space''",color='yellow'), 
                        Tex(r' called the'),
                        Tex(r'\textit{state space}',color='yellow'),
                        Tex(r' of that system. The system is completely'),
                        Tex(r'described by the '),
                        Tex(r'\textit{state vector,}',color='yellow'),
                        Tex(r' a unit vector in the state space.')
        ]
        isolated_quantum_system = statement[1]
        hilbert_space = statement[3]
        state_space = statement[5]
        state_vector = statement[8]
        postulate = Group(title,*statement)
        for s in statement:
            s.scale(0.70)
        statement[0].next_to(title)
        statement[1].next_to(statement[0])
        statement[2].next_to(statement[1],direction=0.8*RIGHT)
        statement[3].next_to(statement[2],direction=0.8*RIGHT)
        statement[4].next_to(statement[0],direction=DOWN,aligned_edge=LEFT)
        statement[5].next_to(statement[4],direction=0.8*RIGHT)
        statement[6].next_to(statement[5],direction=0.8*RIGHT)
        statement[7].next_to(statement[4],direction=DOWN,aligned_edge=LEFT)
        statement[8].next_to(statement[7],direction=0.8*RIGHT)
        statement[9].next_to(statement[8],direction=0.8*RIGHT)
        
        # Display the postulate statement
        self.play(Write(title))
        self.play(*[FadeIn(s) for s in statement])
        self.wait(1)

        # Move the postulate to the top of the screen
        self.play(ApplyMethod(postulate.shift, UP))
        self.wait(1)

        # Highlight and explain isolated quantum system
        self.highlight_and_explain(isolated_quantum_system, r"We're only studying the system in question,\\ ignoring everything else.")

        # Highlight and explain Hilbert Space
        self.highlight_and_explain(hilbert_space,"A complex vector space with an inner product.")

        # Highlight and explain state space
        self.highlight_and_explain(state_space,"The Hilbert space for the system we're studying.")

        # Highlight and explain state vector
        self.highlight_and_explain(state_vector, "The vector that describes the system at any given time.")
        
        # Clear the screen
        self.play(FadeOutAndShiftDown(postulate))

        self.wait(1)

    def highlight_and_explain(self, base, definition):
        title = base.copy()
        self.play(ApplyMethod(title.move_to,ORIGIN), ApplyMethod(base.scale,1.1))
        defn = Tex(definition).next_to(title,direction=DOWN)
        self.play(Write(defn))
        self.wait(1)
        group = Group(title, defn)
        self.play(FadeOut(group),ApplyMethod(base.scale,1.0/1.1))
        self.wait(1)

class Vectors(Scene):
    def construct(self):
        pass

    def ComplexVectorSpaces(self):

        pass

    def IntroduceKets(self):
        # Usually people write vectors with arrow, in quantum computing, instead of arrows, we write kets
        
        # and we usually name our state vectors 'psi' because that's how Schrodinger did it
        pass

    def InnerProducts(self):
        pass

    def Bases(self):
        pass