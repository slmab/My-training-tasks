# TODO здесь писать код

class MyDict(dict):
    def get(self, key, default=0):
        # TODO super(). -- здесь как раз нужен
        return dict.get(self, key, default)

person = MyDict(name='Sergey', age=24)
print(person.get('job'))
