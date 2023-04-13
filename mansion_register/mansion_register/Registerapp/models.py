from django.db import models
from django.db.models.base import Model


class Registerform(models.Model):
    Enter_Your_Name = models.CharField(max_length=30)
    Phone_Number = models.IntegerField()
    Enter_Your_Father_Name = models.CharField(max_length=30)
    Father_Phone_No = models.IntegerField()
    Permanent_Address = models.CharField(max_length=100)
    #Select_Student_or_Employee = models.CharField(max_length=2, choices= Stu_Emp_choise)
    stuEmp_choice = (
            ('Student', 'Student'),
            ('Employee', 'Employee'),
        )
    Select_Student_or_Employee = models.CharField(max_length=30, blank=True, null=True, choices=stuEmp_choice)
    Enter_Name_of_Your_Organization = models.CharField(max_length=100)
    #Emergency_Contact_Per = models.CharField(max_length=2,choices= Emer_Contect_Person)
    emerContact_choice = (
            ('Relative', 'Relative'),
            ('Friend', 'Friend'),
        )
    Emergency_Contact_Per = models.CharField(max_length=30, blank=True, null=True, choices=emerContact_choice)
    Enter_their_name = models.CharField(max_length=30)
    Contact_No = models.IntegerField()
    #Choose_Room_No = models.CharField(max_length=5, CharField=Choose_RoomNo)
    RoomNO_choice = (
            ('Room No.1', 'Room No.1'),
            ('Room No.2', 'Room No.2'),
            ('Room No.3', 'Room No.3'),
            ('Room No.4', 'Room No.4'),
            ('Room No.5', 'Room No.5'),
        )
    Choose_Room_No = models.CharField(max_length=30, blank=True, null=True, choices=RoomNO_choice)
    Date_Of_Joining = models.DateField()
    Rent_Amount_Paid = models.IntegerField()
    
    def __str__(self):
        return self.Enter_Your_Name