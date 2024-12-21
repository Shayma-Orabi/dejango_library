from django import forms 
from . models import Author, Book

class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'placeholder':'enter first name',
            #'name':"first_name",
            #'required':''

        })
        self.fields["last_name"].widget.attrs.update({
            'placeholder':'enter last name'
        })
        self.fields["birthday"].widget.attrs.update({
            'placeholder':'1/1/2000'
        })
        self.fields["description"].widget.attrs.update({
            'placeholder':'any description'
        })
    
    class Meta:
        model = Author
        fields= ['first_name','last_name','birthday','description']
        # widgets ={
        #     'first_name': forms.TextInput(attrs={'placeholder':'enter first name'}),
        #     'last_name': forms.TextInput(attrs={'placeholder':'enter last name'}),
        #     'birthday': forms.DateField(attrs={'placeholder':'enter barthday'},required=True),
        #     'description':forms.Textarea(attrs={'placeholder':'any description'}),
        # }

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["title"].widget.attrs.update({
            'placeholder':'enter title',
            #'name':"first_name",
            #'required':''
        })
        self.fields["genre"].widget.attrs.update({
            'placeholder':'enter genre'
        })
        self.fields["section"].widget.attrs.update({
            'placeholder':'enter section'
        })
        self.fields["version"].widget.attrs.update({
            'placeholder':0
        })
        self.fields["description"].widget.attrs.update({
            'placeholder':'any description'
        })
    
    class Meta:
        model = Book
        fields= ['title','genre','version','section','description']
        