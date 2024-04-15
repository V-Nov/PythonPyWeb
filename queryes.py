import django
import os
import datetime
from django.db.models import Count
from django.db.models import Avg, Q
from django.db.models import Max, Min

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)

    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)

    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))  # Аналогично exact
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))

    # print(Entry.objects.filter(headline__contains='мод'))

    # print(Entry.objects.filter(id__in=[1, 3, 4]))
    # print(Entry.objects.filter(number_of_comments__in='123'))

    # inner_qs = Blog.objects.filter(name__contains='Путешествия')
    # entries = Entry.objects.filter(blog__in=inner_qs)
    # print(entries)

    # print(Entry.objects.filter(number_of_comments__gt=10))
    # print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    # print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
    # print(Entry.objects.filter(headline__lte="Зя"))

    # print(Entry.objects.filter(headline__startswith='Как'))
    # print(Entry.objects.filter(headline__endswith='ния'))

    # start_date = datetime.date(2023, 1, 1)
    # end_date = datetime.date(2023, 12, 31)
    # print(Entry.objects.filter(pub_date__range=(start_date, end_date)))
    # print(Entry.objects.filter(pub_date__year=2023))

    # print(Entry.objects.filter(pub_date__year__lt=2022))
    # print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))
    # print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(
    #     pub_date__day__lte=15).values_list("author__name").distinct())
    # print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))

    # print(Entry.objects.filter(pub_date__date=datetime.date(2021, 6, 1)))
    # print(Entry.objects.filter(pub_date__date__gt=datetime.date(2024, 1, 1)))
    # print(Entry.objects.filter(pub_date__time=datetime.time(12, 00)))
    # print(Entry.objects.filter(pub_date__time__range=(datetime.time(6), datetime.time(17))))

    # print(AuthorProfile.objects.filter(city__isnull=True))

    # print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)'))
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)').distinct())

    # all_obj = Blog.objects.all()
    # print("Вывод всех значений в таблице Blog\n", all_obj)
    # all_obj = Blog.objects.first()
    # print("Вывод первого значения в таблице Blog\n", all_obj)

    # all_obj = Blog.objects.all()
    # obj_first = all_obj.first()
    # print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
    #       f"Все значения = {all_obj}")

    # all_obj = Blog.objects.all()
    # for idx, value in enumerate(all_obj):
    #     print(f"idx = {idx}, value = {value}")
    # print(all_obj[0])  # Получение 0-го элемента
    # print(all_obj[2:4])  # Получение 2 и 3 элемента
    # """Получение последнего элемента не осуществимо через обратный индекс
    # all_obj[-1] - нельзя
    # можно воспользоваться latest('<name_field>'), где <name_field> - имя колонки в БД.
    #
    # Почти все операции над БД не требуют предварительного получения всех элементов, постоянная запись Blog.objects.all()
    # просто для примера.
    # """
    # print(all_obj.latest("id"))  # Получение последнего элемента
    # print(Blog.objects.latest("id"))  # Одинаково работает

    # Пример получения элемента по одному условию
    # print(Blog.objects.get(id=1))
    # Пример получения элемента по двум условиям. Условия работают с оператором И, т.е. выведется строка, только с
    # совпадением и первого и второго параметра.
    # print(Blog.objects.get(id=1, name="Путешествия по миру"))
    # Если нет совпадений, то выйдет исключение "db.models.Blog.DoesNotExist: Blog matching query does not exist."
    # print(Blog.objects.get(id=2, name="Путешествия по миру"))

    # try:
    #     Blog.objects.get(id=2, name="Путешествия по миру")
    # except Blog.DoesNotExist:
    #     print("Не существует")
    # # Пример для filter
    # print(Blog.objects.filter(id=2, name="Путешествия по миру").exists())

    # entry = Blog.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries')
    # print(entry)

    # # Вычислить среднюю оценку только для уникальных значений
    # average_rating = Entry.objects.aggregate(
    #     average_rating1=Avg('rating', distinct=True)
    # )
    # print(average_rating)  # {'average_rating1': 3.6999999999999993}
    #
    # # Вычислить среднюю оценку с заданным значением по умолчанию(допустим
    # # значение у поля None), если агрегация не возвращает результат
    # average_rating_with_default = Entry.objects.aggregate(
    #     average_rating2=Avg('rating', default=5.0)
    # )
    # print(average_rating_with_default)  # {'average_rating2': 3.46}
    #
    # # Вычислить среднюю оценку только для статей, опубликованных после 2023 года
    # average_rating = Entry.objects.aggregate(
    #     average_rating3=Avg('rating', filter=Q(pub_date__year__gt=2023)))
    # print(average_rating)  # {'average_rating3': 2.925}

    # # Вычислить максимальную и минимальную оценку
    # calc_rating = Entry.objects.aggregate(
    #     max_rating=Max('rating'), min_rating=Min('rating')
    # )
    # print(calc_rating)  # {'max_rating': 5.0, 'min_rating': 0.0}




