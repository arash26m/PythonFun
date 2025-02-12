print("Besmellah")
import pyautogui
import time

def move_mouse_periodically(interval_minutes=0.1, movement_distance=10):
    print("Mouse mover started. Press Ctrl+C to stop.")
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()
            
            # Move the mouse slightly
            pyautogui.moveTo(x + movement_distance, y)
            pyautogui.moveTo(x, y)  # Move back to original position
            
            print(f"Mouse moved at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(interval_minutes * 60)  # Wait for the specified interval
    except KeyboardInterrupt:
        print("\nMouse mover stopped.")

# Run the function with a 5-minute interval
move_mouse_periodically()
