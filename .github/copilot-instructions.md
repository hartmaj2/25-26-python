# AI Coding Agent Instructions for 25-26 Python Workspace

## Overview
This repository contains Python-based projects and exercises for educational purposes. The structure includes lesson agendas, example scripts, and specific projects grouped by themes (e.g., Microbit, ZDMSimulace, ZWeby). The workspace is designed to support learning and experimentation with Python programming concepts.

## Key Directories
- **Agendas/**: Contains markdown files outlining lesson plans and schedules.
- **Files/**: Organized by date, this directory includes Python scripts for specific lessons or exercises.
- **Microbit/**: Scripts related to Microbit programming.
- **Ukazky/**: Example Python scripts demonstrating various concepts.
- **ZDMSimulace/**: Scripts for simulations and mathematical explorations.
- **ZWeby/**: Scripts for web scraping and automation.

## Developer Workflows
### Running Python Scripts
1. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```
2. Run the desired Python script:
   ```bash
   python path/to/script.py
   ```

### Testing
- No dedicated test framework is set up. Testing is typically manual by running scripts and observing outputs.

### Debugging
- Use print statements or Python's built-in `pdb` module for debugging.

## Project-Specific Conventions
- **File Organization**: Files are grouped by date or theme for easy navigation.
- **Naming**: Scripts and directories use descriptive names to indicate their purpose.
- **Lists for Pedagogy**: Many scripts use lists to demonstrate fundamental programming concepts.

## Integration Points
- **Microbit**: The `Microbit/` directory contains scripts for interacting with Microbit devices. Ensure the device is connected and the appropriate libraries are installed.
- **Web Automation**: The `ZWeby/` directory includes scripts for web scraping. These may require external libraries like `requests` or `BeautifulSoup`.

## Examples
### Quiz Program
The `Files/26_02_13/quiz.py` script demonstrates a 10-round quiz using lists to store questions and answers. It tracks the score and calculates the average time per question.

### Simulation
The `ZDMSimulace/monty.py` script simulates the Monty Hall problem, showcasing probability concepts.

## External Dependencies
- A virtual environment is included in the `env/` directory. Activate it before running scripts to ensure all dependencies are available.

## Notes
- Follow the structure and conventions in existing scripts when adding new ones.
- Document any new scripts or workflows in the appropriate directory.

---
This guide is a starting point. Update it as the project evolves to ensure AI agents and developers remain productive.