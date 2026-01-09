from django import forms

from .models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название товара"})
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание товара"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control-file"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите стоимость товара"})

    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in self.forbidden_words:
            if word.lower() in name.lower():
                self.add_error("name", f"Название содержит запрещенное слово: {word}")
            if word.lower() in description.lower():
                self.add_error("description", f"В описании содержится запрещенное слово: {word}")

        return cleaned_data

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")

        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

    def clean_image(self):
        cleaned_data = super().clean()
        image = cleaned_data.get("image")

        if image:
            if not image.name.lower().endswith((".jpg", ".png", ".jpeg")):
                raise forms.ValidationError("Недопустимый формат файла. Загрузите JPG или PNG")

            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise forms.ValidationError("Размер изображения должен быть больше 5 МБ")
        return image
