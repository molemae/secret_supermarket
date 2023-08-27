# Secret Supermarket Simulation

Welcome to the Secret Supermarket Simulation project! This repository contains a simulation of customer behavior in a supermarket using a Markov Chain approach. This project was part of my Data Science Bootcamp in Spring 2023.

## Aim of the Project

The primary aim of this project is to simulate and analyze customer behavior within a supermarket environment. The simulation is based on Markov Chain principles, where customers transition between different locations within the supermarket according to defined probabilities. In addition to the simulation, this project emphasizes the following objectives:

1. **Collaborative Working with Git**: The project's second level goal was to improve the student's collaborative development skills using Git and GitHub, allowing multiple contributors to work together on the same codebase.

2. **Object-Oriented Programming (OOP)**: The  project was designed using object-oriented programming principles. Classes and objects are utilized to model the supermarket, customers, and their interactions, resulting in a structured and modular codebase.

## Project Components

- **Data**: The `data` directory contains customer behavior data and related files required for the simulation. This includes CSV files representing customer behavior on different days as well as the calculated transition probability matrices and output data.

- **EDA**: The `EDA` (Exploratory Data Analysis) directory includes the `milestone1.ipynb` Jupyter Notebook files for analyzing the data. The `entry_prob_computation.ipynb` notebook focuses on exploring the entry probabilities, while the `main.py` and `utils.py` files contain the code for calculating the customer transition matrix.

- **Secret Supermarket Simulator**: The `secret_supermarket_simulator` directory contains Python files that implement the simulation using object-oriented programming.
    - `customer.py`: Defines the `Customer` class responsible for modeling customer behavior and transitions.
    - `supermarket.py`: Defines the `Supermarket` class that manages the simulation, customers, and time progression.
    - `super_simulator.py`: The main script that initiates and runs the simulation.

## Running the Simulation

To run the simulation, execute the `super_simulator.py` script located in the `secret_supermarket_simulator` directory. The script simulates customer behavior, updates their locations, and outputs the results to the `entry_prob` directory.

 ## Collaborators
 - [Himansu](https://github.com/TunaHim)
 - [Maryam]
 - [Moritz](https://github.com/MoLeMae)