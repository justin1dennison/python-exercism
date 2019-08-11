def sound_maker(divisor, noise):
    def sounder(n):
        return noise if n % divisor == 0 else ''
    return sounder

pling = sound_maker(3, 'Pling')
plang = sound_maker(5, 'Plang')
plong = sound_maker(7, 'Plong')

def convert(number):
    return ''.join(
        sound(number) for sound in (pling, plang, plong)
    ) or str(number)
