import os
import django

os.environ['DJANGO_SETTINGS_MODULE']='ProTwo.settings'

django.setup()
from AppTwo.models import User
from faker import Faker

fakegen=Faker()

def add_user(N=5):
    for _ in range(N):
        user=User.objects.get_or_create(first_name=fakegen.first_name(),last_name=fakegen.last_name(),email=fakegen.email())[0]
        user.save()
        print (user.first_name)
    
    
if  __name__=='__main__':
    print('populating')
    
    add_user(20)
    
    print('done populating!!')
    