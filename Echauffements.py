def salutation(nom, age):
    message = f"Bonjour '{nom}', vous avez actuellement {age} ans."
    return message

def check_ip_formatp(ip):
    adresse = ip.split('.')
    if len(adresse) != 4:
        return False
    for i in adresse:
        try:
            num = int(i)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    
    return True


def produce_default_dict():
    default_dict = {'root': 'password'}
    return default_dict

def power_2(limit):
    return [2**i for i in range(int(limit) + 1) if 2**i <= int(limit)]

print(power_2(20))