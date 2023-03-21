from django.shortcuts import render

# Create your views here.
from products.models import Product, Comment
from .forms import CommentForm


def product_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                product=product
            )
            comment.save()

    comments = Comment.objects.filter(product=product)

    context = {
        'product': product,
        'comments': comments,
        'form': form,
    }
    return render(request, 'product_detail.html', context)
