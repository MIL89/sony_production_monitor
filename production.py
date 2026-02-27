class Machine:
    # Possible machine states
    allowed_states = {"PRODUCING", "IDLE", "STARVED"}

    def __init__(self, machine_name):
        self.machine_name = machine_name
        self._current_state = "IDLE"  # default state
        self._subscribers = []  # employees observing this machine

    def attach(self, staff_member):
        # Add staff if not already subscribed
        if staff_member not in self._subscribers:
            self._subscribers.append(staff_member)

    def unsubscribe(self, staff_member):
        # Remove staff from notification list
        if staff_member in self._subscribers:
            self._subscribers.remove(staff_member)

    def change_state(self, new_state):
        new_state = new_state.upper()

        # Validate state
        if new_state not in self.allowed_states:
            raise ValueError(f"{new_state} is not a valid machine state.")

        # Only notify if state actually changes
        if new_state != self._current_state:
            self._current_state = new_state
            self._notify_staff()

    def _notify_staff(self):
        # Inform all subscribed staff members
        for staff in self._subscribers:
            staff.receive_update(self.machine_name, self._current_state)

    def get_state(self):
        return self._current_state
