class Lab:
  def __init__(self, roomNumber):
    self.roomNumber = roomNumber


class Technician:
  assigned_lab = None
  def __init__(self, name):
    self.name = name
  def assign_lab(self, lab_obj):
    self.assigned_lab = lab_obj

chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)
print(mr_cruz.assign_lab.room_number)
