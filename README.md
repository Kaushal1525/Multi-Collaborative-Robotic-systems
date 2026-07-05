
# Obstacle Detection and Avoidance Module for Multi-Collaborative Robotic System (MCRS)

## Overview

This project implements a simulated Obstacle Detection and Avoidance module designed for the Multi-Collaborative Robotic System (MCRS). The module continuously monitors the distance between a robot and surrounding obstacles using simulated sensor readings and determines the appropriate navigation response.

The system categorizes obstacle proximity into multiple safety levels and performs corresponding actions such as safe navigation, avoidance maneuvers, or emergency stopping. Audible alerts are generated for critical situations to emulate real-world robotic safety systems.

This project demonstrates one of the core perception and safety modules required for autonomous mobile robots and collaborative robotic fleets.

---

## Features

- Real-time obstacle distance monitoring
- Simulated proximity sensor readings
- Multi-level obstacle classification
- Automatic obstacle avoidance logic
- Emergency stop detection
- Audible warning alerts
- Terminal-based monitoring dashboard
- Continuous autonomous operation
- Lightweight simulation

---

## Technologies Used

- Python 3
- Colorama
- Winsound
- Random
- Time

---

## Project Structure

```text
MCRS-Obstacle-Detection/
│
├── obstacle_detection.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Kaushal1525/MCRS-Obstacle-Detection.git
```

### Navigate to the project directory

```bash
cd MCRS-Obstacle-Detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the application:

```bash
python obstacle_detection.py
```

The program continuously generates simulated obstacle distance values and displays the robot's navigation status.

Terminate the simulation by pressing:

```text
Ctrl + C
```

---

## Working Principle

The obstacle detection module performs the following sequence:

1. Generate simulated obstacle distance measurements.
2. Compare the measured distance against predefined safety thresholds.
3. Determine the current obstacle risk level.
4. Trigger the appropriate navigation response.
5. Generate audible alerts during emergency conditions.
6. Continue monitoring until manually terminated.

---

## Obstacle Classification

| Distance | Robot Response |
|----------|----------------|
| Greater than 20 cm | Safe navigation |
| 10–20 cm | Obstacle avoidance maneuver |
| Less than or equal to 10 cm | Emergency avoidance with audible alert |

---

## System Workflow

```text
Obstacle Sensor
        │
        ▼
Distance Measurement
        │
        ▼
Safety Threshold Evaluation
        │
        ▼
Decision Making
        │
        ├──────────────► Safe Navigation
        │
        ├──────────────► Avoidance Maneuver
        │
        └──────────────► Emergency Stop and Warning
```

---

## Safety Levels

### Safe Navigation

The detected obstacle is outside the safety threshold.

The robot continues normal operation.

---

### Warning Zone

An obstacle is detected within the caution range.

The robot initiates an avoidance maneuver to maintain a safe path.

---

### Critical Zone

An obstacle is detected extremely close to the robot.

The system:

- Generates an emergency warning
- Activates an audible alert
- Initiates emergency avoidance

---

## Applications

- Autonomous Mobile Robots
- Multi-Collaborative Robotic Systems (MCRS)
- Warehouse Automation
- Service Robotics
- Industrial Mobile Robots
- Smart Manufacturing
- Autonomous Delivery Robots
- Swarm Robotics
- Robotics Research
- Autonomous Navigation

---

## Future Enhancements

- Ultrasonic sensor integration
- LiDAR-based obstacle detection
- Camera-based object detection
- Sensor fusion
- Dynamic obstacle avoidance
- Path replanning using A*
- ROS 2 integration
- Gazebo simulation
- SLAM integration
- Multi-robot collision avoidance
- Reinforcement learning-based navigation
- Autonomous fleet coordination

---

## Requirements

- Python 3.8 or later
- Colorama

---

## Dependencies

- colorama

> Note: The `winsound` module is included with Python on Windows systems and does not require separate installation.

---

## Author

Kaushal Reddy

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
````
