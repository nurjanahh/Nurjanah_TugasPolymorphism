class Indonesia:
    def ibu_kota(self):
        print("DKI Jakarta adalah ibu kota dari indonesia.")
  
    def bahasa(self):
        print("Bahasa Indonesia adalah bahasa nasional indonesia.")
  
    def type(self):
        print("Indonesia termasuk negara berkembang.")
  
class Jepang():
    def ibu_kota(self):
        print("Tokyo adalah ibu kota dari Jepang.")
  
    def bahasa(self):
        print("Bahasa Jepang adalah bahasa nasional Jepang.")
  
    def type(self):
        print("Jepang termasuk negara maju.")
 
def func(obj):
    obj.ibu_kota()
    obj.bahasa()
    obj.type()
  
obj_ind = Indonesia()
obj_jpn = Jepang()
  
func(obj_ind)
func(obj_jpn)