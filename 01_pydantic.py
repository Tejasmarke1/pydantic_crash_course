from pydantic import AnyUrl, BaseModel,EmailStr,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title="Name of the patient",description="Give the name of the patient in less than 50 characters",examples=["Ayush","Nitish"])]
    age: int =Field(gt=0 ,lt=120,title="Age of the patient",description="Age of the patient must be between 1 and 119")
    email:EmailStr=Field(description="Email of the ")
    linkedIn_url:AnyUrl
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Annotated[bool,Field(default=None,description="Is the patient married?")]
    allergies:Optional[List[str]]= Field(max_length=5)
    contacts: Dict[str, str]

    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("inserted into database")
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("inserted into database")
    
Patient_info={'name': "ayush", 'age':30,'email':"abc@gmail.com",'linkedIn_url':"https://www.linkedin.com/in/tejas-marke/",'weight': 70.5,'married': True,
              'allergies': ['pollen', 'nuts'],
              'contacts': {'home': '123-456-7890', 'work': '098-765-4321'}} 

patient1=Patient(**Patient_info)


# insert_patient_data(patient1)

update_patient_data(patient1)