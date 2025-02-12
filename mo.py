print("Besmellah")
import pyautogui
import time

def move_periodically(interval_minutes=0.1, movement_distance=10):
    print("mover started. Press Ctrl+C to stop.")
    try:
        while True:
            # Get current position
            x, y = pyautogui.position()
            
            # Move slightly
            pyautogui.moveTo(x + movement_distance, y)
            pyautogui.moveTo(x, y)  # Move back to original position
            
            print(f"Moved at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(interval_minutes * 60)  # Wait for the specified interval
    except KeyboardInterrupt:
        print("\nMover stopped.")
        
move_periodically()
