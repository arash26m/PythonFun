print("Besmellah")

import pyautogui
import time

def move_mouse_and_click(duration_hours=2, interval_minutes=2):
    # Calculate total duration in seconds
    total_duration = duration_hours * 60 * 60
    # Calculate interval in seconds
    interval_seconds = interval_minutes * 60
    # Start time
    start_time = time.time()
    
    print(f"Starting mouse movement and clicking for {duration_hours} hours.")
    while time.time() - start_time < total_duration:
        # Move the mouse to a random position near the current position
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 10, y + 10, duration=0.5)
        pyautogui.moveTo(x, y, duration=0.5)
        
        # Perform a left click
        pyautogui.click()
        print("Mouse moved and clicked.")
        
        # Wait for the interval
        time.sleep(interval_seconds)
    
    print("Finished mouse movement and clicking.")

if __name__ == "__main__":
    move_mouse_and_click()

