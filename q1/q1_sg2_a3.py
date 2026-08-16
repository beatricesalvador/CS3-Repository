while True:
    birth = input("Enter your year of birth: ")
    
    if not birth.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    
    birth = int(birth)
  
    signs = [
    "Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"
    ]
    
    if birth >= 1900:
        remainder = (birth - 1900) % 12
        print("Your Chinese Zodiac Sign is:", signs[remainder])
      
    else:
        print("Invalid input. It should not be earlier than 1900.")
    break

    
  

    
      
