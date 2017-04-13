from django import forms, modelformset_factory

from .models import Product, Category


class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = ("category")


	def clean(self):
		category = self.cleaned_data.get("category")
		if category:
			qs = Category.objects.filter(category_iexact=category)
			if self.instance.pk is not None:
				qs = qs.exclude(pk=self.instance.pk)
			if qs.exists():
				self.add_error("category", "This category already existed")

		return self.cleaned_data


class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ("product")

	def clean(self):
		product = self.cleaned_data.get("product")
		if product:
			qs = Product.objects.filter(product_iexact=product)
			if self.instance.pk is not None:
				qs = qs.exclude(pk=self.instance.pk)
			if qs.exists():
				self.add_error("product", "This product doesnot exist")

		return self.cleaned_data


CategoryFormset = modelformset_factory(Category, CategoryForm, min_num=2, extra=0)
ProductFormset = modelformset_factory(Product, ProductForm, min_num=2, extra=0)