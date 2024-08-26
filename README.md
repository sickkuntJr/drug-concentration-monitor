# Drug Concentration Monitor

This project is a Python application with a graphical user interface (GUI) for monitoring drug concentration in the blood over time. The user can input dosages, specify the time of administration (in days and hours), and the half-life of the drug. The application calculates the drug concentration over a 10-day period and displays it on a graph, divided into 24-hour segments with labels for each day.

## Features

- **Add Dosages**: Input drug dosages with the relevant details, including day, hour, amount, and half-life.
- **Modify/Remove Dosages**: Easily modify or remove dosages from the list.
- **Graphical Display**: View drug concentration over time with a clear graph segmented into days.
- **Interactive List**: Manage your dosages via a list that updates the graph in real-time.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sickkuntJr/drug-concentration-monitor.git
    cd drug-concentration-monitor
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script using Python:

```bash
python main.py
