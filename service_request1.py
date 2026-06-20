class Farmer:
	def __init__(self, farmer_id, name, phone, village, crop):
		self.farmer_id = farmer_id
		self.name = name
		self.phone = phone
		self.village = village
		self.crop = crop


class Technician:
	def __init__(self, technician_id, name, skill, area):
		self.technician_id = technician_id
		self.name = name
		self.skill = skill
		self.area = area


class ServiceRequest:
	def __init__(self, request_id, farmer, service_type, description):
		self.request_id = request_id
		self.farmer = farmer
		self.service_type = service_type
		self.description = description
		self.status = "Pending"
		self.technician = None


class FarmerServiceRequestSystem:
	def __init__(self):
		self.farmers = []
		self.requests = []
		self.technicians = [
			Technician(1, "Ramesh Kumar", "Irrigation Repair", "North Zone"),
			Technician(2, "Suresh Patel", "Tractor Repair", "East Zone"),
			Technician(3, "Anita Singh", "Pest Control", "South Zone"),
		]

	def _generate_id(self, prefix, items):
		return f"{prefix}{len(items) + 1:03d}"

	def add_farmer(self):
		print("\n--- Add Farmer Details ---")
		name = input("Enter farmer name: ").strip()
		phone = input("Enter phone number: ").strip()
		village = input("Enter village name: ").strip()
		crop = input("Enter crop name: ").strip()

		farmer_id = self._generate_id("F", self.farmers)
		farmer = Farmer(farmer_id, name, phone, village, crop)
		self.farmers.append(farmer)

		print(f"Farmer added successfully. Farmer ID: {farmer_id}")

	def _select_farmer(self):
		if not self.farmers:
			print("No farmers found. Please add a farmer first.")
			return None

		print("\nAvailable Farmers:")
		for index, farmer in enumerate(self.farmers, start=1):
			print(f"{index}. {farmer.farmer_id} - {farmer.name} ({farmer.village})")

		try:
			choice = int(input("Select farmer number: "))
			if 1 <= choice <= len(self.farmers):
				return self.farmers[choice - 1]
		except ValueError:
			pass

		print("Invalid farmer selection.")
		return None

	def create_service_request(self):
		print("\n--- Create Service Request ---")
		farmer = self._select_farmer()
		if farmer is None:
			return

		service_type = input("Enter service type: ").strip()
		description = input("Enter request description: ").strip()

		request_id = self._generate_id("R", self.requests)
		request = ServiceRequest(request_id, farmer, service_type, description)
		self.requests.append(request)

		print(f"Service request created successfully. Request ID: {request_id}")

	def assign_request(self):
		print("\n--- Assign Request to Local Technician ---")
		pending_requests = [request for request in self.requests if request.status == "Pending"]

		if not pending_requests:
			print("No pending requests available for assignment.")
			return

		for index, request in enumerate(pending_requests, start=1):
			print(
				f"{index}. {request.request_id} - {request.farmer.name} - {request.service_type}"
			)

		try:
			request_choice = int(input("Select request number: "))
			if not (1 <= request_choice <= len(pending_requests)):
				raise ValueError

			request = pending_requests[request_choice - 1]
		except ValueError:
			print("Invalid request selection.")
			return

		print("\nAvailable Technicians:")
		for index, technician in enumerate(self.technicians, start=1):
			print(
				f"{index}. {technician.technician_id} - {technician.name} | {technician.skill} | {technician.area}"
			)

		try:
			tech_choice = int(input("Select technician number: "))
			if not (1 <= tech_choice <= len(self.technicians)):
				raise ValueError

			technician = self.technicians[tech_choice - 1]
		except ValueError:
			print("Invalid technician selection.")
			return

		request.technician = technician
		request.status = "Assigned"
		print(
			f"Request {request.request_id} assigned to {technician.name} successfully."
		)

	def view_all_requests(self):
		print("\n--- View All Requests ---")
		if not self.requests:
			print("No service requests found.")
			return

		for request in self.requests:
			technician_name = request.technician.name if request.technician else "Not Assigned"
			print("-" * 50)
			print(f"Request ID   : {request.request_id}")
			print(f"Farmer       : {request.farmer.name} ({request.farmer.farmer_id})")
			print(f"Phone        : {request.farmer.phone}")
			print(f"Village      : {request.farmer.village}")
			print(f"Crop         : {request.farmer.crop}")
			print(f"Service Type : {request.service_type}")
			print(f"Description  : {request.description}")
			print(f"Technician   : {technician_name}")
			print(f"Status       : {request.status}")

	def update_request_status(self):
		print("\n--- Update Request Status ---")
		if not self.requests:
			print("No requests available.")
			return

		for index, request in enumerate(self.requests, start=1):
			technician_name = request.technician.name if request.technician else "Not Assigned"
			print(
				f"{index}. {request.request_id} - {request.farmer.name} - {request.status} - {technician_name}"
			)

		try:
			choice = int(input("Select request number: "))
			if not (1 <= choice <= len(self.requests)):
				raise ValueError
			request = self.requests[choice - 1]
		except ValueError:
			print("Invalid request selection.")
			return

		print("\nAvailable Status Options:")
		status_options = ["Pending", "Assigned", "In Progress", "Completed", "Cancelled"]
		for index, status in enumerate(status_options, start=1):
			print(f"{index}. {status}")

		try:
			status_choice = int(input("Select new status: "))
			if not (1 <= status_choice <= len(status_options)):
				raise ValueError
			request.status = status_options[status_choice - 1]
		except ValueError:
			print("Invalid status selection.")
			return

		print(f"Request {request.request_id} status updated to {request.status}.")

	def run(self):
		while True:
			print("\n=== Farmer Service Request Management System ===")
			print("1. Add Farmer Details")
			print("2. Create Service Request")
			print("3. Assign Request to Local Technician")
			print("4. View All Requests")
			print("5. Update Request Status")
			print("6. Exit")

			choice = input("Enter your choice: ").strip()

			if choice == "1":
				self.add_farmer()
			elif choice == "2":
				self.create_service_request()
			elif choice == "3":
				self.assign_request()
			elif choice == "4":
				self.view_all_requests()
			elif choice == "5":
				self.update_request_status()
			elif choice == "6":
				print("Exiting system. Goodbye!")
				break
			else:
				print("Invalid choice. Please try again.")


if __name__ == "__main__":
	system = FarmerServiceRequestSystem()
	system.run()
	# test