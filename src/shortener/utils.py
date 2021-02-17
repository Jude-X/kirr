import string
import random


def code_generator(size=6, chars=string.ascii_letters+string.digits):
    code = ''.join(random.choice(chars) for _ in range(size))
    print('judex.ly/'+code)
    return 'judex.ly/'+code


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)
    Klass = instance.__class__
    exists = Klass.objects.filter(shortcode=new_code).exists()
    if exists:
        return create_shortcode(size=size)
    return new_code
