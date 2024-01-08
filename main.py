import init_django_orm  # noqa: F401

from db.models import Car, Message, Company, Person


def car_main():
    car = Car.objects.create(
        brand="Skoda",
        horsepower=220,
        creation_date="2020-01-01",
        # description="No, this is the best car you ever seen",
        market_segment="C"

    )
    print(car)


def message_main():
    message = Message.objects.create(
        content=" MESSAGE 4 ",
    )
    print(message.__dict__)


def company_main():
    Company.objects.create(
        name="SHMOOGLE",
        description="ANOTHER company"
    )
    print("Companies : ", Company.objects.all())


def person_main():
    # person = Person.objects.get(name="John")
    # person.id = None
    # person.save()

    person = Person.objects.get(id=1)
    person.delete()



if __name__ == '__main__':
    person_main()
