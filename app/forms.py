from django import forms
from .models import Post, GrandCategory, ParentCategory


class PostCreateForm(forms.ModelForm):
    grand_category = forms.ModelChoiceField(
        label='大カテゴリー',
        queryset=GrandCategory.objects,
        required=False
    )
    # 親カテゴリの選択欄がないと絞り込めないので、定義する。
    parent_category = forms.ModelChoiceField(
        label='中カテゴリー',
        queryset=ParentCategory.objects,
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

    field_order = ('title', 'grand_category', 'parent_category', 'category')
