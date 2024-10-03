from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseSlugModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        count = 0
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += f'_{count}'
            count += 1
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,update_fields=update_fields)

    class Meta:
        abstract = True


class BaseCreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseSlugModel, BaseCreatedModel):
    def __str__(self):
        return self.name


class Product(BaseSlugModel, BaseCreatedModel):
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

# a = Category.objects.first()
















