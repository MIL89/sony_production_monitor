from production import Machine
from staff import StaffMember


def main():
    # Creating machines
    cutter = Machine("Cutter Machine")
    packer = Machine("Packaging Unit")

    # Creatin staff members list
    supervisor = StaffMember("Milly Francis", "Production Supervisor")
    technician = StaffMember("James Carter", "Maintenance Technician")

    # Subscribing staff to machines
    cutter.attach(supervisor)
    cutter.attach(technician)
    packer.attach(technician)

    # Simulating state changes
    cutter.change_state("PRODUCING")
    packer.change_state("STARVED")
    cutter.change_state("IDLE")


if __name__ == "__main__":
    main()
