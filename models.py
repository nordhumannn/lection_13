from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)


class Dish(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}$'

    class Meta:
        ordering = ('position', 'price')
        
#--------------------------------------------------------

class Dish(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    ingredients = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    special = models.BooleanField(default=False)
    image = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.price}$'

    class Meta:
        ordering = ('position', 'price')
        index_together = (('id', 'slug'),)
        
#------------------------------------------------------


class Event(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    price = models.FloatField()
    description = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}, {self.price}, {self.description}'


class Gallery(models.Model):
    image = models.ImageField()
