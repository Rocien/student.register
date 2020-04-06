from django import forms 
from .models import Student

# This is the student form
class StudentForm(forms.ModelForm):

    # Meta class for how ModelForm "Student" is shown on the page
    class Meta:
        model = Student
        fields = ('name','surname','mobile','address','grade') #field order on the page
        
        # Labels to modify the field titles ex. starting with capital letters
        labels = {
            'name':'Name',
            'surname':'Surname',
            'mobile':'Mobile',
            'address':'Address',
            'grade':'Grade',
        }
        
    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['grade'].empty_label = 'Select'         #Adding "select" on the grade fields
        self.fields['grade'].required = False               # This is to remove the field fill requirement sign "*"