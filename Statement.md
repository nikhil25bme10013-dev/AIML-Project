# Project Statement — AI Dice Battle (CustomTkinter GUI)

## Introduction

AI Dice Battle is a turn-based dice combat game developed in Python with a graphical user interface built using the CustomTkinter library. The project demonstrates how simple game mechanics, when combined with a clean GUI and structured logic, can create an engaging user experience.

The objective of the game is straightforward: the player and an AI opponent take turns rolling dice, and the higher score in each round deals damage to the other. The first to reduce the opponent’s health points (HP) to zero wins.

This project focuses on combining game logic, probability, decision-making, and GUI design into a cohesive application.

---

## Objectives

The main objectives of this project are:

- To design a turn-based game using Python
- To implement a graphical interface using CustomTkinter 
- To separate game logic from user interface code
- To demonstrate basic AI decision-making
- To create an interactive and user-friendly desktop application

---

## Game Mechanics

Each round consists of:

1. The player choosing to roll either 2 or 3 dice
2. The AI selecting its dice count based on current HP conditions
3. Both sides calculating scores from their dice rolls
4. Damage being applied based on the score difference

Special scoring rules add unpredictability:

- Rolling two sixes grants a bonus
- Rolling any one results in a penalty

These rules encourage strategic choices between safe and risky moves.

---

## Technical Design

The project is structured to keep logic and interface separate:

- Core game functions handle dice rolling, scoring, and AI decisions
- A GUI class manages all visual components and user interaction
- State variables track HP, rounds, and game progress
 
This separation improves readability, maintainability, and scalability.

---

## Tools and Technologies

- Python 3
- CustomTkinter for GUI
- Random module for dice simulation

---

## Learning Outcomes

Through this project, the following concepts are demonstrated:

- Event-driven programming with GUI frameworks
- Object-oriented design
- Game loop control without a console
- Simple artificial intelligence logic
- User interface state management

---

## Conclusion

AI Dice Battle is a compact yet complete example of how Python can be used to create interactive desktop games with a modern interface. The project balances simplicity in rules with thoughtful design, making it both educational and enjoyable to use.
