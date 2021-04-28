# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Import statements

# %%
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# %% [markdown]
# # 2D

# %%
class FR_2d():
    def __init__(self, grid_min, grid_max, res=1000):
        self.grid_min = grid_min
        self.grid_max = grid_max
        self.res = res
        self.grid = np.linspace(grid_min, grid_max, self.res)
        self.x1, self.x2 = np.meshgrid(self.grid, self.grid)
        self.constraints = np.ones(shape=(self.res, self.res))
        self.plots = []
    
    def add_constraint(self, c):
        global constraints
        self.constraints =  np.logical_and(self.constraints,c)

    def plot(self):
        extent = x1.min(),x1.max(),x2.min(),x2.max()
        plt.figure(figsize=(14,8))
        plt.imshow(self.constraints,
                   extent=extent,
                   origin="lower",
                   cmap="Greys",
                   alpha = 0.3)
        
fr1 = FR_2d(-1, 13)
x1 = fr1.x1
x2 = fr1.x2

# Add constraints here
fr1.add_constraint(x1 + x2<=14)
fr1.add_constraint(-2*x2<=4-x1)
fr1.add_constraint(x2<=-.2*x1+8)
fr1.add_constraint(x2>=-20*x1+59)

fr1.plot()

# %% [markdown]
# # 3D

# %%
# define all constraints
def constraints(x,y,z):
    return np.all([
        x - 2*y <= 2,
        x + y >= 0,
        y >= 0,
    ])


# %%
grid_res = 15 
x_grid = np.linspace(-10, 10, grid_res)
y_grid = np.linspace(-10, 10, grid_res)
z_grid = np.linspace(-10, 10, grid_res)

X = np.array([])
Y = np.array([])
Z = np.array([])

for x in x_grid:
    for y in y_grid:
        for z in z_grid:
            if constraints(x,y,z):
                X = np.append(X, x)
                Y = np.append(Y, y)
                Z = np.append(Z, z)
            
fig = go.Figure(data=[go.Mesh3d(x=X, y=Y, z=Z, alphahull=0, opacity=.8)])
fig


# %%



# %%



# %%



# %%



# %%



# %%



# %%



