class User:
    _user_list = []

    _name_ = ""
    _age_ = ""

    @property # getter
    def age(self):
        return self._age_
    @age.setter # setter
    def age(self, _age_):
        self._age_ = _age_

    @classmethod
    def speak(cls):
        return len(cls._user_list)

    def _private_seename(self):
        print self._name_
        pass

    def __strong_private_seeage(self):
        print self._age_

u = User()
print(u._private_seename())
# print(u.__strong_private_seeage)
#print(dir())
u._age_="20"
print(u.age)

class MyMath:
    @staticmethod
    def triangle(base, height):
        return base * height / 2

print(MyMath.triangle(20, 100))

class MyIterable:
    def __init__(self, x):
        self.step = 0
        self.x = x
    def __iter__(self):
        self.step = 0
        return self
    def next(self):
        if self.step > self.x:
            raise StopIteration
        self.step += 1
        return 1


mi = MyIterable(3)
for n in mi:
    for m in mi:
        print(n, m)
