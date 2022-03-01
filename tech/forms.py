from Django import froms
from .models import TechType, Product, Review

class ProductForm(modelsForm):
    class Meta:
        model=Product
        fields='__all__'

