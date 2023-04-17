from manim import *
import numpy as np

class StockPrice(Scene):
    def construct(self):
        # Define parameters
        S0 = 40  # initial stock price
        r = 0.05  # risk-free interest rate
        sigma = 0.3  # volatility
        T = 2  # time horizon
        N = 2000  # number of time steps
        dt = T / N  # time increment

        # Generate stock price using geometric Brownian motion
        t = np.linspace(0, T, N+1)
        W = np.random.standard_normal(size=N+1)
        Q = np.random.standard_normal(size=N+1)
        W = np.cumsum(W)*np.sqrt(dt)  # Brownian motion
        X = (r - 0.5 * sigma**2) * t + sigma * W
        S = S0 * np.exp(X)  # stock price

        Q =  np.cumsum(Q)*np.sqrt(dt)
        X1 = (r - 0.5 * sigma**2) * t + sigma * Q
        S1 = S0*np.exp(X1)
        
        # Create axes
        axes = Axes(
            x_range=[0, T, 0.1],
            y_range=[-30,80, 10],
            x_axis_config={
                "numbers_to_include": np.arange(0, T+0.1, 0.1),
                "decimal_number_config": {"num_decimal_places": 1}
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 200+10, 10)
            }
        )
        self.add(axes)

          # x_min must be > 0 because log is undefined at 0.
        graph = axes.plot(lambda x: S[int(x*N/T)])
        grap_1 =axes.plot(lambda x: S1[int(x*N/T)])
        spread = axes.plot(lambda x: S[int(x*N/T)]- S1[int(x*N/T)])


        graph.set_color(BLUE)
        grap_1.set_color(ORANGE)
        spread.set_color(GRAY)
        self.play(Create(graph),Create(grap_1),Create(spread),run_time=20)
        #self.add(axes,graph)
        # Add labels
        #title = Text("Simulated Stock Price", font_size=36).next_to(axes.y_axis, UP)
        #self.play(Write(title))

        #x_label = axes.get_x_axis_label("Time (years)")
        #y_label = axes.get_y_axis_label("Price ($)")
        #self.play(Write(x_label), Write(y_label))

        #self.wait()

