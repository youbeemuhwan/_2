import json
import re
from django.http import JsonResponse

from django.views import View
from owners.models import Owner, Dog


class owner_signup_view (View):
    def post(self, request) :
        data = json.loads(request.body)
        Owner.objects.create(
            name = data["name"],
            email = data["email"],
            age = data["age"]
        )
        
        return JsonResponse({'messasge':'created'},status=201)
    
    
    def get(self, request) :
        
        owners=Owner.objects.all()
        result = []
        for owner in owners:
            dogs= owner.dog_set.all()
            owners_dog =[]
            for dog in dogs :
                owners_dog.append({
                    "name" : dog.name,
                    "age" : dog.age,
                }
                )
            result.append(
                {   'name' : owner.name,
                    'email' : owner.email,
                    'age' : owner.age,
                    'dog' : owners_dog,
                    
                }
            )
        return JsonResponse({"result": result}, status=201)
                
            
            
            
            

        
        
        
        
        
                
        return JsonResponse({'results':result},status=201)
    
        
class dog_signup_view(View) :
    def post(self, request) :
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data["owner"])
        Dog.objects.create(
            
            name = data["name"],
            age=data["age"],
            owner = owner,
        
        )
        return JsonResponse({'messasge':'created'},status=200)
    
    def get(self, request) :
        dog_list = Dog.objects.all()
        result= []
        
        for dog in dog_list:
            result.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name,
                }
            )
         
        return JsonResponse({'result':result},status=200)
        
        
        

# Create your views here.
