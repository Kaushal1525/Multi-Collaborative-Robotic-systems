import random
import time
from colorama import Fore, Style, init
import winsound

# Initialize Colorama
init(autoreset=True)

def get_obstacle_distance():
    """Simulates obstacle distance readings (in cm)."""
    return random.randint(5, 100)

def obstacle_detection():
    print(Fore.CYAN + "\n🚧 Starting Obstacle Detection & Avoidance...\n")
    try:
        while True:
            distance = get_obstacle_distance()

            if distance <= 10:
                print(Fore.RED + f"[Obstacle] 🚨 Critical! Obstacle Very Very Close -> {distance} cm")
                winsound.Beep(1000, 500)  # Beep only in critical condition
                print(Fore.RED + "⚡ Emergency Avoidance Activated! ⚡\n")
                time.sleep(1)

            elif distance <= 20:
                print(Fore.YELLOW + f"[Obstacle] ⚠️ Warning! Obstacle Very Close -> {distance} cm")
                print(Fore.YELLOW + "⚠️ Executing Avoidance Maneuver...\n")
                time.sleep(1)

            else:
                print(Fore.GREEN + f"[Obstacle] ✅ Path is Clear -> Distance: {distance} cm\n")

            time.sleep(1)

    except KeyboardInterrupt:
        print(Fore.RED + "\nObstacle Detection stopped manually.")

if __name__ == "__main__":
    try:
        obstacle_detection()
    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram manually stopped.")
