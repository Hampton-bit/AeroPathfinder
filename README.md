# AeroPathfinder
This project integrates Dijkstra's algorithm into a Flight Management System (FMS) to optimize route planning, aiming for a 20% reduction in flight durations and a 15% decrease in fuel consumption. It enhances operational efficiency, while providing an educational tool for Data Structures and Algorithms.

## Abstract
This project focuses on integrating Dijkstra's algorithm into a Flight Management System (FMS) to optimize route planning in aviation. By leveraging the algorithm's ability to find the shortest path in a graph, we aim to enhance route planning efficiency while considering factors like aircraft performance, weather, and airspace constraints. The project involves implementing Dijkstra's algorithm, developing a user-friendly interface for real-time interaction, and visualizing computed routes. The anticipated outcomes include improved flight efficiency, reduced fuel consumption, and enhanced safety, serving as an educational tool for demonstrating practical applications of Dijkstra's algorithm in aviation and Data Structures and Algorithms coursework.

## Table of Contents
- [1. Introduction](#1-introduction)
  - [1.1 Problem Statement](#11-problem-statement)
  - [1.2 Overview](#12-overview)
- [2. Methodology](#2-methodology)
  - [2.1 Block Diagram and Explanation](#21-block-diagram-and-explanation)
  - [2.2 Modules](#22-modules)
  - [2.3 GUI Implementation](#23-gui-implementation)
- [3. Conclusion](#3-conclusion)
- [4. References](#4-references)

## 1. Introduction

### 1.1 Problem Statement
Current flight management systems lack efficient route planning algorithms, leading to increased fuel consumption and longer flight durations. Manual processes are error-prone and do not adapt to real-time changes like weather or airspace restrictions. This project aims to develop a Flight Management System using Dijkstra's algorithm to optimize routes, addressing inefficiencies, real-time adaptability, user interaction, and educational integration.

### 1.2 Overview
Flight management systems (FMS) are vital for modern aviation, yet existing systems often struggle to efficiently optimize flight routes. This project proposes integrating Dijkstra's algorithm, a cornerstone of Data Structures and Algorithms (DSA) courses, into FMS to address these challenges. Dijkstra's algorithm, known for finding the shortest path in a graph, offers a solution for optimizing routes while considering various factors like aircraft performance, weather conditions, and airspace constraints.

## 2. Methodology

### 2.1 Block Diagram and Explanation
The project integrates Dijkstra's algorithm into a Flight Management System (FMS) to optimize route planning for aircraft. The system takes input parameters from users, including departure and destination airports, aircraft characteristics, and real-time weather data. It applies Dijkstra's algorithm to compute the optimal route, considering these factors, and displays the computed route through a user-friendly interface.

### 2.2 Modules
The methodology is broken down into the following modules:

1. **Imports:**
   - Libraries such as `tkinter`, `heapq`, `matplotlib.pyplot`, and `networkx` are imported for GUI, priority queue, graph plotting, and graph operations, respectively.

2. **Class Definitions:**
   - **Passenger:** Represents a passenger with attributes.
   - **ListNode:** Represents a node in a linked list.
   - **LinkedList:** Implements a linked list for passenger records.
   - **Queue:** Represents a queue for managing a waiting list.
   - **Graph:** Models flight connections between airports.
![image](https://github.com/user-attachments/assets/e9c83cd9-0e70-4611-9aa6-f0971c77e7c1)

3. **Dijkstra Algorithm:**
   - Implements the shortest path function to find the shortest route between airports.

4. **Utility Functions:**
   - Functions to load airport data, check seat availability, and manage booking history.

5. **Ticket Booking System Classes:**
   - Manages passenger bookings, ticket history, and waiting lists.

6. **Main Application Class:**
   - Initializes the GUI and manages navigation.

7. **Start Page:**
   - Provides options for listing airports, checking availability, and booking tickets.

8. **Main Program Execution:**
   - Initializes the application and starts the event loop.

### 2.3 GUI Implementation
The user interface is built using Tkinter, facilitating interaction with the system for tasks such as airport selection, ticket booking, and checking seat availability. Visualization of the flight map enhances user experience.

## 3. Conclusion
Integrating Dijkstra's algorithm into the Flight Management System represents a significant advancement in optimizing route planning for aircraft. The project successfully addresses challenges in route optimization, real-time adaptability, and educational integration within aviation.

## 4. References
- [Dijkstra's Shortest Path Algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
