from django import forms

class Arac(forms.Form):
    hiz = forms.IntegerField(label='Hız')
    zaman = forms.IntegerField(label='Zaman (saat)')
    depo = forms.IntegerField(label='Depo (litre)')
    
    def __init__(self, *args, **kwargs):
        super(Arac, self).__init__(*args, **kwargs)
        self.yol = 0

    def sur(self):
        hiz = int(self.data['hiz'])
        zaman = int(self.data['zaman'])
        self.yol = hiz * zaman
        self.kalanDepo = self.kalan_depo()
        self.kalanDepo -= (self.yol/100)*self.ortalama_yakit()        
        return self.kalanDepo
    
    def gidilenYol(self):
        return self.yol

    def kalan_depo(self):     
        if hasattr(self, 'kalanDepo'):
            return self.kalanDepo
        else:
            self.kalanDepo = int(self.data['depo'])
            return self.kalanDepo        

    def menzil(self):        
        return int(100*(self.kalan_depo()/self.ortalama_yakit()))
    
    def ortalama_yakit(self):
        ortalama_hiz = int(self.data['hiz'])
        if ortalama_hiz <= 100:
            return 7
        elif ortalama_hiz <= 130:
            return 8
        elif ortalama_hiz <= 150:
            return 9
        elif ortalama_hiz <= 180:
            return 10
        elif ortalama_hiz <= 200:
            return 12
        else:
            return 15
