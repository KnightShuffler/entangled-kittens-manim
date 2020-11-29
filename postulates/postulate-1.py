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

class DiracNotation(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\newcommand{ket}{1}{\left|#1\right\rangle')
        title = Tex('Dirac Notation for Vectors').to_edge(UP)
        # Change arrow to ket
        #~  usually people denote vectors by drawing an arrow above the vector's name
        vec = MathTex(r'\vec{v}','=',r'\begin{bmatrix} v_0 \\ v_1 \\ v_2 \\ v_3 \end{bmatrix}')
        self.play(Write(title),FadeInFrom(vec,direction=UP))
        self.wait(1)
        
        #~  in quantum computing literature, we denote vectors by surrounding the vector by an arrow' and calling them kets
        ket_v = MathTex(r'|v\rangle').move_to(vec[0],aligned_edge=RIGHT)
        ket = MathTex('\\ket{\\cdot} - \\text{``ket\'\'}',color='yellow').to_corner(UR).shift(0.5*DOWN)
        self.play(ReplacementTransform(vec[0],ket_v),FadeIn(ket))
        self.wait(1)


        #~  We write the standard basis vectors as kets named by the position the '1' is in (starting our indexing from 0)
        group1 = Group(ket_v,vec)
        basis = [
            MathTex(r'\ket{0} = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix},'),
            MathTex(r'\ket{1} = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix},'),
            MathTex(r'\ket{2} = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix},'),
            MathTex(r'\ket{3} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}'),
        ]
        for i in range(1,len(basis)):
            basis[i].next_to(basis[i-1],direction=1.1*RIGHT,aligned_edge=LEFT)
        group2 = Group(*basis)
        group2.move_to(ORIGIN + 2*DOWN)
        
        self.play(ApplyMethod(group1.shift,UP),FadeIn(group2))
        self.wait(1)
        
        #~  And instead of column matrices, we usually write vectors as linear combinations of the basis kets
        sum = MathTex(r'v_0\ket{0} + v_1\ket{1} + v_2\ket{2} + v_3\ket{3}').move_to(vec[1].get_edge_center(RIGHT)+0.2*RIGHT,aligned_edge=LEFT).shift(2*LEFT)
        self.remove(ket_v)
        self.play(ApplyMethod(vec[0].shift,2*LEFT),ApplyMethod(vec[1].shift,2*LEFT),ReplacementTransform(vec[2],sum))
        self.wait(1)

        self.play(FadeOutAndShift(Group(title,vec,group2,sum,ket),direction=DOWN))

class DotProduct(Scene):
    def construct(self):
        #~  "To be considered a Hilbert space, we also need to define an inner product
        #~  "In real vector spaces, we have a dot product which is defined as so:
        # Write title
        real_title = Tex('Real Vector Spaces').to_edge(UP)
        # Write vectors to screen
        vec_v = MathTex(r'\vec{v}','=',r'\begin{bmatrix} v_0 \\ v_1 \\ \vdots \\ v_{N-1} \end{bmatrix}',color='#75dc84')
        vec_w = MathTex(',',r'\vec{w}','=',r'\begin{bmatrix} w_0 \\ w_1 \\ \vdots \\ w_{N-1} \end{bmatrix}',color=LIGHT_PINK).next_to(vec_v)
        vec_group = VGroup(vec_v,vec_w).scale(0.8).move_to(ORIGIN)

        v_matrix = vec_v[2]
        w_matrix = vec_w[3]

        self.play(Write(real_title),FadeInFrom(vec_group,direction=UP))
        self.wait(1)

        # Write dot product definition
        dot_product = MathTex(r'\vec{v}',r'\cdot',r'\vec{w}',
                                '=',
                                r'\vec{v}^T',
                                r'\vec{w}',
                                '=',
                                r'\sum_{k=0}^{N-1}','v_k', 'w_k').move_to(ORIGIN+0.5*DOWN)
        dot_product[0].set_color('#75dc84')
        dot_product[2].set_color(LIGHT_PINK)
        vT = dot_product[4].set_color('#75dc84')
        w  = dot_product[5].set_color(LIGHT_PINK)
        dot_product[-2].set_color('#75dc84')
        dot_product[-1].set_color(LIGHT_PINK)
        self.play(ApplyMethod(vec_group.move_to,real_title.get_edge_center(DOWN)+(vec_group.get_height()/2 + 0.2)*DOWN),
                FadeInFrom(dot_product,direction=DOWN))
        self.wait(1)
        vT_matrix = MathTex(r'\begin{bmatrix}v_0 & v_1 & \dots & v_{n-1}\end{bmatrix}',color='#75dc84').scale(0.8)
        w_Copy = w_matrix.copy().next_to(vT_matrix)
        vTw_group = VGroup(vT_matrix,w_Copy).next_to(dot_product,direction=DOWN)
        self.play(ApplyMethod(vT.scale,1.2),ReplacementTransform(vT.copy(),vT_matrix))
        self.wait(1)
        self.play(ApplyMethod(vT.scale,1.0/1.2),ApplyMethod(w.scale,1.2),ReplacementTransform(w.copy(),w_Copy))
        self.play(ApplyMethod(w.scale,1.0/1.2))
        self.wait(1)

        # Move real group to the side
        real_group = VGroup(real_title,vec_group,dot_product,vTw_group)
        self.play(real_group.to_edge,LEFT)
        self.wait(1)

        # Now repeat for complex spaces
        #~  "For complex vector spaces, we define the dot product very similarly
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r'\newcommand{ket}{1}{\left|#1\right\rangle')
        myTemplate.add_to_preamble(r'\newcommand{bra}{1}{\left\langle#1\right|')
        myTemplate.add_to_preamble(r'\newcommand{braket}{2}{\left\langle#1\right|\left.#2\right\rangle')

        complex_title = Tex('Complex Vector Spaces').to_edge(UP)
        ket_v = MathTex(r'\ket{v}=',r'\begin{bmatrix} v_0 \\ v_1 \\ \vdots \\ v_{N-1} \end{bmatrix}',color='#75dc84')
        ket_w = MathTex(r',\ket{w}=',r'\begin{bmatrix} w_0 \\ w_1 \\ \vdots \\ w_{N-1} \end{bmatrix}',color=LIGHT_PINK).next_to(ket_v)
        ket_group = VGroup(ket_v,ket_w).scale(0.8).move_to(ORIGIN)

        v_matrix = ket_v[1]
        w_matrix = ket_w[1]

        cdot_product = MathTex(r'\ket{v}',r'\cdot',r'\ket{w}', '=',
                                r'\ket{v}^\dagger',
                                r'\ket{w}',
                                r'=\sum_{k=0}^{N-1}', r'v_k^*', r'w_k').move_to(ORIGIN+0.5*DOWN)
        cdot_product[0].set_color('#75dc84')
        cdot_product[2].set_color(LIGHT_PINK)
        v_bra = cdot_product[4].set_color('#75dc84')
        w_ket = cdot_product[5].set_color(LIGHT_PINK)
        cdot_product[-2].set_color('#75dc84')
        cdot_product[-1].set_color(LIGHT_PINK)

        vDagger_matrix = MathTex(r'\begin{bmatrix}v_0^* & v_1^* & \dots & v_{N-1}^*\end{bmatrix}',color='#75dc84').scale(0.8)
        wMatrix_copy = w_matrix.copy().next_to(vDagger_matrix)
        vDw_group = VGroup(vDagger_matrix,wMatrix_copy).next_to(cdot_product,direction=DOWN)

        complex_group = VGroup(complex_title,ket_group,cdot_product,vDw_group).to_edge(RIGHT)

        #~  "For complex vector spaces..."
        self.play(Write(complex_title),FadeInFrom(ket_group,direction=UP))
        self.wait(1)
        #~  "we take the complex conjugate of each element when we transpose the matrix,
        #   this conjugate transpose is called the adjoint or the Hermitian conjugate"
        self.play(ApplyMethod(ket_group.move_to,complex_title.get_edge_center(DOWN)+(ket_group.get_height()/2 + 0.2)*DOWN),
                FadeInFrom(cdot_product,direction=DOWN))
        self.wait(1)
        self.play(ApplyMethod(v_bra.scale,1.1),
            ReplacementTransform(v_bra.copy(),vDagger_matrix))
        self.wait(1)
        self.play(ApplyMethod(v_bra.scale,1.0/1.1),
            ApplyMethod(w_ket.scale,1.1),
            ReplacementTransform(w_ket.copy(),wMatrix_copy))
        self.play(ApplyMethod(w_ket.scale,1.0/1.1))
        self.wait(1)
        adjoint_note = MathTex(r"{}^\dagger-\text{``adjoint''}",color='yellow').to_corner(UR).shift(0.5*DOWN)
        complex_group.remove(complex_title)
        self.play(FadeOutAndShift(real_group,direction=DOWN),
            ApplyMethod(complex_group.to_edge,LEFT),
            ApplyMethod(complex_title.move_to, np.array([0,complex_title.get_center()[1], complex_title.get_center()[2]])),
            FadeIn(adjoint_note))
        self.wait(1)

        #~  "We can rewrite the adjoint of a ket like this, and we call it a bra"
        bra_v = MathTex(r'\bra{v}',color='#75dc84').next_to(w_ket,direction=LEFT,aligned_edge=RIGHT).shift(0.2*LEFT)
        bra_note = VGroup(MathTex(r"\bra{\cdot}-\text{``bra''}",color='yellow'),
                        MathTex(r'\bra{v} = \ket{v}^\dagger',color='yellow'))
        bra_note[1].next_to(bra_note[0],direction=DOWN)
        bra_note.next_to(adjoint_note,direction=DOWN,aligned_edge=RIGHT)
        self.play(ReplacementTransform(v_bra,bra_v),FadeIn(bra_note))
        self.wait(1)

        #~  "And we can write the dot product like this as a shorthand"
        braket = MathTex(r'\bra{v}',r'w\rangle').move_to(cdot_product[2],aligned_edge=RIGHT)
        braket[0].set_color('#75dc84')
        braket[1].set_color(LIGHT_PINK)
        braket_note = MathTex(r'\braket{v}{w} = \ket{v}\cdot\ket{w}',color='yellow').next_to(bra_note,direction=DOWN,aligned_edge=RIGHT)
        cdot = Group(cdot_product[0],cdot_product[1],cdot_product[2])
        self.play(ReplacementTransform(cdot,braket),FadeIn(braket_note))
        self.wait(1)

        self.remove(braket)
        self.remove(bra_v)
        self.play(FadeOutAndShift(Group(ket_group,vDw_group),direction=DOWN),
            ApplyMethod(cdot_product.shift,2.5*UP))
        self.wait(1)
        #~  "Let's take an example in Dirac notation"




class Qubits(Scene):
    def construct(self):
        pass
