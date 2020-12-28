from django import forms


class kontakForm(forms.Form):
    nama_lengkap = forms.CharField()

    GENDER = [('P', 'Pria'), ('W', 'Wanita')]
    jenis_kelamin = forms.ChoiceField(choices=GENDER)

    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1999, 2022, 1)))

    email = forms.EmailField()
    alamat = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField()
