#Types of variables and methods in oops

#types of varaibles in oops
#1.instance variables - which will be created inside a constructor can be accessed only by the instances
#2.class/static variables - these are  created in a class which can be access by the all instances of that object and also with the class name


#types of methods in oops
#1.instance method - this method which have only the instance variables
#2.class method - this method which does not have any instance variables
#3.static method - in this method it does not have any variables

#object/instance - we can call all methods (instance,class,static)
#class_name - we can call the class and static methods except instance method

class StudentsDetails:

    school_name = 'Ravindra School' #class/static variables
    principal = 'Ram Mohan Naidu'
    vice_principal = 'chitra shetty'

    def __init__(self,roll_no,st_name,st_standard,grade):
        self.roll_no = roll_no # instance variables
        self.name = st_name
        self.standard = st_standard
        self.grade = grade

    print(f'Student Basic details:')
    def student_details(self): #instance method (only will use of instance variables)
        print(f'st_roll_no:{self.roll_no},st_name:{self.name},st_standard:{self.standard},st_grade:{self.grade}')

    @classmethod #there will be no single instance variable in class method 
    def additional_info(cls,activity,sports):
        cls.curicular_activity = activity
        cls.sports = sports
        print(f'st_suricular_activity:{cls.curicular_activity},st_sports:{cls.sports}')

    @staticmethod #there will be no variables in static method
    def about_school():
        print(f'This school is in top 10 category list')
        print(f'It also secured a A++ grade from NAAC New Delhi')

#student1 details
st1 = StudentsDetails(1,'sai','VI','B')
st1.student_details() #calling instance method using instance object with instance variables

print(f'shool_name:{st1.school_name}') #accessing class/static variable using instance object
print(f'principal_name:{st1.principal}')
print(f'vice_principal:{st1.vice_principal}')
st1.about_school() #accessing static method using instance object

st1.additional_info('good','exellent') #accessing class method using instance object

# StudentsDetails.student_details(st1) #calling instance method with the class name


st2 = StudentsDetails(2,'raghu','VI','A')
st2.student_details() #calling instance method using instance object with instance variables

print(f'shool_name:{StudentsDetails.school_name}') #accessing class/static variable using class name
print(f'principal_name:{StudentsDetails.principal}')
print(f'vice_principal:{StudentsDetails.vice_principal}')
StudentsDetails.about_school() #accessing static method using class name

StudentsDetails.additional_info('poor','good') #accessing class method using class name

# StudentsDetails.student_details(st2) #calling instance method with the class name
