import networkx as nx
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import math
from menu import *
from colorama import init, Fore

class Pandemic: # Class used for configuring the pandemic and its parameters.
    def __init__(self, network):
        self.steps = 9
        self.infection = 0.7
        self.recovery = 0.3
        self.network = network
        self.graph = network.graph()
        self.colors = {'S': 'blue', 'I': 'red', 'R': 'green', 'D': 'grey'}
        self.pos = nx.spring_layout(self.graph, seed=42)
        self.state = {}
        self.history = {'S': [], 'I': [], 'R': [], 'D': []}

    def initializeState(self):
        # This function initializes the states that will later be used to display the pandemic.
        self.state = {n: 'S' for n in self.graph.nodes()}
        initial_node = random.choice(list(self.graph.nodes()))
        self.state[initial_node] = 'I'

    def generate_pandemic_evolution(self):
        # This method coordinates the execution of other methods to ensure a structured workflow.
        self.initializeState()
        self.updateHistory()
        self.simulate()

    def updateHistory(self):
        # This function records the history of states to later plot them.
        counts = {'S': 0, 'I': 0, 'R': 0, 'D': 0}
        for state in self.state.values():
            counts[state] += 1
        for key in self.history:
            self.history[key].append(counts[key])

    def simulate(self):
        # This function compiles all time steps into a visual representation to illustrate the progression of the pandemic across the network.
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
        # This function randomly assigns a type to each node based on the input infection and recovery parameters, distinguishing between susceptible, infected, recovered, and deceased individuals.
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
        # This function changes the node's colors based on the state at each step.
        ax.clear()
        node_colors = [self.colors[self.state[n]] for n in self.graph.nodes()]
        nx.draw(self.graph, pos=self.pos, ax=ax, with_labels=True, node_color=node_colors, node_size=600)
        ax.set_title(f"Step {step}")
        ax.set_axis_off()

        rect = patches.Rectangle(
            (0, 0), 1, 1, transform=ax.transAxes,
            linewidth=2, edgecolor='black', facecolor='none'
        )
        ax.add_patch(rect)

    def plotStateEvolution(self):
        # This function plots the temporal evolution of the SIRD model
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
