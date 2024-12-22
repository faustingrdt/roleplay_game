import random
import sys

life_me = 50
life_enemy = 50

potion = 3

choice_expected = ["1", "2"]

while True :
    choice_player = input("Souhaitez-vous attaquer (1) ou utiliser un potion (2) : ")
    
    if not choice_player in choice_expected :
        print("entrer une valeur valide 🙄")   
        
    if choice_player == "1" :
        
        attack_enemy = random.randrange(5,16)
        attack_by_me = random.randrange(5,11)
        
        life_enemy -= attack_by_me
        life_me -= attack_enemy
        
        print(f"Votre ennemie vous a infligé {attack_enemy}")
        print(f"Vous avez infligé {attack_by_me} à l'ennemi")
        
        
        print(f"Votre enemie a {life_enemy} pv")
        print(f"Vous avez {life_me} pv")
        
        if life_enemy <= 0 :
            print("Bravo vous avez gagné 🤘 !!!")
            sys.exit()
        
        elif life_me <= 0 :
            print("Vous avez perdu 🤕")
            sys.exit()
            
        print(f"Votre enemie a {life_enemy} pv")
        print(f"Vous avez {life_me} pv")
        print("-----------------")
    
    if choice_player == "2" :
        
        if potion > 0 :
            pv_health = random.randrange(15, 51)
            life_me = min(life_me + pv_health , 50)
            
            potion -= 1
            
            print(f"Vous avez récupérer {pv_health}pv")
            print(f"Votre vie : {life_me}")
            print(f"Il vous reste {potion} potion{"s" if potion > 1 else ""}")
       
            
            attack_enemy = random.randrange(5,16)
            life_me -= attack_enemy
            print(f"Votre ennemie vous a infligé {attack_enemy}")
            print(f"Vous avez {life_me} pv")
        
            print("-----------------")
        else :
            print("vous n'avez plus de potions...")
            print("-----------------")
        
        

      