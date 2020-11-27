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
        self.play(FadeOutAndShift(self.highlight_and_explain(isolated_quantum_system, r"We're only studying the system in question,\\ ignoring everything else."),direction=DOWN),
            ApplyMethod(isolated_quantum_system.scale,1.0/1.1))
        self.wait(1)

        # Highlight and explain Hilbert Space
        hilbert_group = self.highlight_and_explain(hilbert_space,"A complex vector space with an inner product.")
        vec = MathTex(r'\vec{v} = ',r'\begin{bmatrix} 1 \\ \frac{\pi}{7} \\ -1 \end{bmatrix}').next_to(hilbert_group,direction=1.5*DOWN)
        self.play(Write(vec))
        self.wait(1)
        vec2 = MathTex(r'\begin{bmatrix} 1 + 2i \\ e^{i\frac{\pi}{7}} \\ -1 + 3i \end{bmatrix}').move_to(vec[1],aligned_edge=LEFT)
        self.play(ReplacementTransform(vec[1], target_mobject=vec2))
        self.wait(1)
        hgroup = Group(hilbert_group,vec,vec2)
        self.play(FadeOutAndShift(hgroup,direction=DOWN),ApplyMethod(hilbert_space.scale,1.0/1.1))
        

        # Highlight and explain state space
        self.play(FadeOutAndShift(self.highlight_and_explain(state_space,"The Hilbert space for the system we're studying."),direction=DOWN),
        ApplyMethod(state_space.scale,1.0/1.1))
        self.wait(1)

        # Highlight and explain state vector
        self.play(FadeOutAndShift(self.highlight_and_explain(state_vector, "The vector that describes the system at any given time."),direction=DOWN),
        ApplyMethod(state_vector.scale,1.0/1.1))
        self.wait(1)
        
        # Clear the screen
        self.play(FadeOutAndShift(postulate),direction=DOWN)

        self.wait(1)

    def highlight_and_explain(self, base, definition):
        title = base.copy()
        self.play(ApplyMethod(title.move_to,ORIGIN), ApplyMethod(base.scale,1.1))
        defn = Tex(definition).next_to(title,direction=DOWN)
        self.play(Write(defn))
        self.wait(1)
        group = Group(title, defn)
        # self.play(FadeOut(group),ApplyMethod(base.scale,1.0/1.1))
        # self.wait(1)
        return group

# Table of contents to be displayed after the postulate statement
class TableOfContents(Scene):
    def construct(self):
        #1 - Dirac Notation for vectors
        #2 - The Complex Dot-Product
        #3 - Quantum Bits
        contents = [
            Tex('1. Dirac Notation for vectors'),
            Tex('2. The Complex Dot Product'),
            Tex('3. Quantum Bits (Qubits)')
            ]
        contents[1].next_to(contents[0],direction=DOWN,aligned_edge=LEFT)
        contents[2].next_to(contents[1],direction=DOWN,aligned_edge=LEFT)
        Group(*contents).move_to(ORIGIN)

        for c in contents:
            self.play(Write(c))
            self.wait(1)
        self.play(FadeOutAndShift(Group(*contents),direction=DOWN))
        self.wait(1)
        
