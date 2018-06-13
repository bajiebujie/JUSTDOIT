#! encoding: utf8
import datetime
import re


class Student(object):
    def __init__(self):
        self._name = ''
        self._birth = ''
        self._age = ''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        if not re.match('[0-9]{4}\.[0-9]{1,2}\.[0-9]{1,2}$', birth):
            raise ValueError('Not valid birth(%s), use [yyyy.mm.dd]' % birth)
        self._birth = birth
        birth_datetime = datetime.datetime.strptime(self._birth, '%Y.%m.%d')
        now = datetime.datetime.now()
        self._age = now.year - birth_datetime.year

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        raise AttributeError('Can not set attribute <age>, should set <birth>')

    def describe(self):
        print self.__str__()

    def __str__(self):
        return 'name=%s, birth=%s, age=%s' % (self.name, self.birth, self.age)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    student = Student()
    # student.describe()
    print student
    student.name = 'hehe'
    student.birth = '1985.12.12'
    student.describe()
    # student.birth = '85.12.12'
    # student.age = 10
    print student
    print `student`
