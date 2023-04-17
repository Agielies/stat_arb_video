from manim import*
import numpy as np
# Generate two correlated random walks



class CoIntegratedPair(Scene):
    def construct(self):
        # Set up axnp.random.seed(42)
        N = 1000
        X = np.cumsum(np.random.randn(N+1))
        Y = np.cumsum(np.random.randn(N+1))
        r = np.corrcoef(X, Y)[0, 1]
        # Compute the spread
        spread = Y - r*X
        axes = Axes(
            x_range=[0, N],
            y_range=[-20, 20],
            x_length= 8,
            y_length = 4,
            axis_config={
                "color": WHITE,
                "stroke_width": 2.0,
                "include_tip": False,
                "label_direction": DOWN
            },
            y_axis_config={
                "label_direction": LEFT
            }
            )

        # Plot the two random walks
        #X_graph = axes.plot(lambda x: X[int(x)], color=ORANGE)
        #Y_graph = axes.plot(lambda x: Y[int(x)], color=BLUE)
        spread_graph = axes.plot(lambda x: spread[int(x)], color=GREY)

        
        x_1 = axes.plot(lambda x: X[int(x)],color = BLUE)
        y_1 = axes.plot(lambda y: Y[int(y)],color = ORANGE)


        self.play(Create(x_1),Create(y_1),Create(spread_graph),run_time=5)
        
        # Plot the spread
       
        # Add labels
        #X_label = axes.get_x_axis_label("X")
        #Y_label = axes.get_x_axis_label("Y")
        #spread_label = axes.get_y_axis_label("Spread")

        # Animate the plot
        #self.add(axes, X_graph, Y_graph, spread_graph)
        #self.play(
        #    DrawBorderThenFill(X_graph),
        #    DrawBorderThenFill(Y_graph),
        #    DrawBorderThenFill(spread_graph),
        #    Write(X_label),
        #    Write(Y_label),
        #    Write(spread_label),
        #    run_time=5)
        self.wait()

