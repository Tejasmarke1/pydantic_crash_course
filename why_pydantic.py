def insert_patient_data(name:str,age: int):
    
    if type(name)==str and type(age)==int:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        else:
            print(f"Inserting patient data: Name={name}, Age={age}")
            print("Patient data inserted successfully.")
        
    else:
        raise TypeError("Invalid data types: Name must be a string and Age must be an integer.")
    
def update_patient_data(name:str,age: int):
    
    if type(name)==str and type(age)==int:
        print(f"updating patient data: Name={name}, Age={age}")
        print("updated patient data successfully.")
        
    else:
        raise TypeError("Invalid data types: Name must be a string and Age must be an integer.")



insert_patient_data("ayush",30)