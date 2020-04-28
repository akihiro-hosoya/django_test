from django.db import models

class GrandCategory(models.Model):
    name = models.CharField('大カテゴリー', max_length=50)
    icon = models.CharField('アイコン', max_length=50)

    def __str__(self):
        return self.name

class ParentCategory(models.Model):
    name = models.CharField('中カテゴリー', max_length=50)
    grand = models.ForeignKey(GrandCategory, verbose_name='大カテゴリー', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('小カテゴリー', max_length=50)
    parent = models.ForeignKey(ParentCategory, verbose_name='中カテゴリー', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)
    category = models.ForeignKey(Category, verbose_name='小カテゴリー', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
