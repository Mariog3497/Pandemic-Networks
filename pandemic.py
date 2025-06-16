import networkx as nx
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import math
from menu import *
from colorama import init, Fore

class Pandemic:
    # Class used to configure the pandemic and its parameters
    def __init__(self, network):
        self.steps = 9  # Number of time steps to simulate
        self.infection = 0.7  # Probability of infection
        self.recovery = 0.3  # Probability of recovery (else: death)
        self.network = network  # Network topology object
        self.graph = network.graph()  # The actual NetworkX graph
        self.colors = {'S': 'blue', 'I': 'red', 'R': 'green', 'D': 'grey'}  # Colors for each state
        self.pos = nx.spring_layout(self.graph, seed=42)  # Position of nodes for visualization
        self.state = {}  # Current state of each node (S, I, R, D)
        self.history = {'S': [], 'I': [], 'R': [], 'D': []}  # Time evolution of states

    def initializeState(self):
        # Initializes the network with all nodes susceptible except one infected
        self.state = {n: 'S' for n in self.graph.nodes()}
        initial_node = random.choice(list(self.graph.nodes()))
        self.state[initial_node] = 'I'

    def generate_pandemic_evolution(self):
        # Orchestrates the simulation steps
        self.initializeState()
        self.updateHistory()
        self.simulate()

    def updateHistory(self):
        # Records the number of nodes in each state at the current time step
        counts = {'S': 0, 'I': 0, 'R': 0, 'D': 0}
        for state in self.state.values():
            counts[state] += 1
        for key in self.history:
            self.history[key].append(counts[key])

    def simulate(self):
        # Main loop for simulating the pandemic over several steps and visualizing it
        cols = 3
        rows = math.ceil(self.steps / cols)

        
        fig1, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
        fig1.canvas.manager.set_window_title("Pandemic Network Simulator")
        fig1.suptitle(
            f"Pandemic Evolution\n"
            f"Infection: {self.infection} | Recovery: {self.recovery}\n"
            f"{self.network}",
            fontsize=16
        )

        # Centers the plot window if using the TkAgg backend
        mng = plt.get_current_fig_manager()
        backend = matplotlib.get_backend()
        if backend == 'TkAgg':
            screen_width = mng.window.winfo_screenwidth()
            screen_height = mng.window.winfo_screenheight()
            fig_width, fig_height = fig1.get_size_inches()
            dpi = fig1.get_dpi()
            window_width = int(fig_width * dpi)
            window_height = int(fig_height * dpi)
            x = int((screen_width - window_width) / 2)
            y = int((screen_height - window_height) / 2)
            mng.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        if rows == 1 and cols == 1:
            axes = [axes]
        else:
            axes = axes.flatten()

        for step in range(self.steps):
            self.drawGraph(axes[step], step)
            self.pandemicStep()

        for i in range(self.steps, len(axes)):
            axes[i].axis('off')

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show(block=False)  

        
        self.plotStateEvolution()

    def pandemicStep(self):
        # Updates the state of the network based on infection and recovery probabilities
        new_state = self.state.copy()

        for node in self.graph.nodes():
            if self.state[node] == 'I':
                for neighbor in self.graph.neighbors(node):
                    if self.state[neighbor] == 'S' and random.random() < self.infection:
                        new_state[neighbor] = 'I'
                if random.random() < self.recovery:
                    new_state[node] = 'R'
                else:
                    new_state[node] = 'D'

        self.state = new_state
        self.updateHistory()

    def drawGraph(self, ax, step):
        # Draws the network at a given time step, coloring nodes by their state
        ax.clear()
        node_colors = [self.colors[self.state[n]] for n in self.graph.nodes()]
        nx.draw(self.graph, pos=self.pos, ax=ax, with_labels=True, node_color=node_colors, node_size=600)
        ax.set_title(f"Step {step}")
        ax.set_axis_off()

        # Add a border around the graph panel
        rect = patches.Rectangle(
            (0, 0), 1, 1, transform=ax.transAxes,
            linewidth=2, edgecolor='black', facecolor='none'
        )
        ax.add_patch(rect)

    def plotStateEvolution(self):
        # Plots the evolution of the number of nodes in each state over time
        steps = list(range(len(self.history['S'])))
        label_map = {
            'S': 'S - Susceptible',
            'I': 'I - Infected',
            'R': 'R - Recovered',
            'D': 'D - Deceased'
        }

        fig2 = plt.figure(figsize=(10, 5))
        fig2.canvas.manager.set_window_title("Pandemic State Evolution")

        for state, values in self.history.items():
            plt.plot(steps, values, label=label_map[state], color=self.colors[state])
        plt.title("Pandemic State Evolution")
        plt.xlabel("Steps")
        plt.ylabel("Number of Nodes")
        plt.legend()
        plt.grid(False)  
        plt.tight_layout()
        plt.show(block=False)
