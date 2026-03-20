import sys
import time
import uiautomator2 as u2

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    # 1. Check for Split-Screen Divider
    # The hierarchy shows the resource ID: com.android.systemui:id/docked_divider_handle
    divider = d(resourceId="com.android.systemui:id/docked_divider_handle")
    time.sleep(2)
    
    if divider.exists:
        print("Split screen detected. Attempting to exit...")
        
        try:
            # Get coordinates of the divider
            bounds = divider.info['bounds']
            center_x = (bounds['left'] + bounds['right']) // 2
            center_y = (bounds['top'] + bounds['bottom']) // 2
            
            # Get screen height to swipe all the way down
            # d.window_size() returns (width, height)
            screen_width, screen_height = d.window_size()
            
            # Perform the swipe: Center of divider -> Bottom of screen
            # This maximizes the top app (Contacts) and dismisses the bottom split
            print(f"Swiping divider from ({center_x}, {center_y}) to ({center_x}, {screen_height})...")
            d.swipe(center_x, center_y, center_x, screen_height, 0.5)
            
            # Wait for animation to complete
            time.sleep(2)
            
        except Exception as e:
            print(f"Error manipulating divider: {e}")
            # Fallback: Attempt to just go home, though this sometimes leaves split screen active
    else:
        print("No split screen divider found.")

    # 2. Return to Home Screen
    # This ensures the device is left in a neutral state
    time.sleep(1)
    print("Going Home...")
    d.press("home")
    time.sleep(1)
    
    print("Cleanup complete.")
