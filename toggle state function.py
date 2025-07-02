#toggle state function
#toggling a global flag
is_active=False
def toggle_state():
    global is_active
    is_active=not is_active
    return is_active
print(f"Initial state:{is_active}")
toggle_state()
print(f"state after 1st toggle:{is_active}")
toggle_state()
print(f"state after 2nd toggle:{is_active}")
toggle_state()
print(f"state after 3rd toggle:{is_active}")