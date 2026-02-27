class StaffMember:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def receive_update(self, machine_name, state):
        print(
            f"{self.position} {self.name} "
            f"has been notified that '{machine_name}' "
            f"is now {state}."
        )
