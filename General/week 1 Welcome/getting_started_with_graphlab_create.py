#!/usr/bin/env python
# -*- coding: utf-8 -*-


# coding: utf-8

## Getting Started with GraphLab Create

# ## First a note about IPython Notebook
# Most of our tutorials are written as IPython notebooks. This allows you to download and run the tutorials on your own machine, either as notebooks (.ipynb) or Python files (.py). To run the notebooks you'll need to install IPython and IPython Notebook; for installation details, visit [www.ipython.org](http://www.ipython.org). A couple of the notebooks depend on [matplotlib](http://matplotlib.org/) for custom plots; this library can be installed with the terminal command 'pip install matplotlib'.
# 
# ## Overview
# In this tutorial, you'll get a good flavor of some of the fundamental tasks that GraphLab Create is built for.
# 
# You will learn how to:
# 
# * load data into SFrames
# * create a Graph data structure from these frames
# * write simple graph queries
# * apply a machine learning model from the Graph Analytics Toolkit
# 
# We also have many other toolkits to explore from including recommender systems, data matching, graph analytics and more. Explore these and the rest of Graphlab Create in our [User Guide](https://dato.com/learn/userguide/). 
# 
# ...oh yeah, you'll also learn that some of us at Dato have a thing for Bond...yes...James Bond...

# In[1]:

import graphlab as gl
gl.canvas.set_target('ipynb') # use IPython Notebook output for GraphLab Canvas


# # Load data into an SFrame
# GraphLab Create uses two scalable data structures:
# 
# - the SFrame, a tabular structure ideal for data munging & feature building
# - the Graph, a structure ideal for sparse data

# In[2]:

vertices = gl.SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_vertices.csv')
edges = gl.SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_edges.csv')


# In[3]:

# SFrame has a number of methods to explore and transform your data
vertices.show()


# In[4]:

# this shows the summary of the edges SFrame
edges.show()


# # Create a graph object

# In[5]:

g = gl.SGraph()


# # Add vertices and edges to this graph

# In[6]:

# add some vertices in a dataflow-ish way
g = g.add_vertices(vertices=vertices, vid_field='name')


# In[7]:

# more dataflow
g = g.add_edges(edges=edges, src_field='src', dst_field='dst')


# # Do some basic graph querying

# In[8]:

# Show all the vertices
g.get_vertices()


# In[9]:

# Show all the edges
g.get_edges()


# In[10]:

# Get all the "friend" edges
g.get_edges(fields={'relation': 'friend'})


# # Apply the pagerank algorithm to our graph

# In[11]:

pr = gl.pagerank.create(g)


# In[12]:

pr.get('pagerank').topk(column_name='pagerank')


# ### We see, not unexpectedly, that James Bond is a very important person, and that bad guys aren't that popular...
# 
# (Looking for more details about the modules and functions? Check out the <a href="https://dato.com/products/create/docs/">API docs</a>.)
