# creat Hospital class
class Hospital:
    # creating Constructor
    def __init__(self,name): # self is a keyword and name is a class parameter
        # Before aqual sign is a class variable and after aqual sign is a class paprameter
        # Explanation: self.name is a class variable and name is a class parameter
        self.name = name
        self.doctors =[] # creating empty list of doctors
        self.patients = [] # creating empty list of patients
    # creating class methods
    # Explanation: jab bhi hum class kai andar koi method banate hai tw  usko hum class metod bolty h.....
    def add_doctor(self,add_doc):
        return self.doctors.append(add_doc)
    
    def remove_doctor(self,remove_doc):
        return self.doctors.remove(remove_doc)
    
    def get_doctor(self):
        return self.doctors
    
    def add_patient(self,add_pat):
        return self.patients.append(add_pat)
    def remove_patient(self,remove_pat):
        return self.patients.remove(remove_pat)
    def get_patient(self):
        return self.patients
# creating class Doctor
class Doctor:
    def __init__(self, name , specialty ,experience):
        self.name = name
        self.specialty = specialty
        self.experience = experience
# creating class patient
class Patient:
    def __init__(self, name , age , diseaes):
        self.name = name
        self.age = age
        self.diseaes = diseaes
# creating object of the class
hospital=Hospital("City Hospital...")
print(hospital.name)
doctor = Doctor("Dr. Smith","Cardiology", 10)
patient = Patient("John Doe", 30, "Heart Disease")
#Add doctor and patient to the hospital class####
print(hospital.add_doctor(doctor.name))
print(hospital.add_patient(patient.name))
print(hospital.get_doctor())
print(hospital.get_patient())
# Doctor list 
doct1 = Doctor("Dr.John","Dentist", 5)
doct2 = Doctor("Dr. Jane" , "Orthopedic", 7)
print(hospital.add_doctor(doct1.name))
print(hospital.add_doctor(doct2.name))
print(hospital.get_doctor())
# Patient list
pat1 = Patient("Alice", 25, "Flu")
pat2 = Patient("Bob", 40, "Diabetes")
print(hospital.add_patient(pat1.name))
print(hospital.add_patient(pat2.name))
print(hospital.get_patient())

# Remove doctor
print(hospital.remove_doctor("Dr. Jane"))
print(hospital.get_doctor())
# Remove patient
print(hospital.remove_patient("John Doe"))
print(hospital.get_patient())