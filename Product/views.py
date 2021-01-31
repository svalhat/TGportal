from django.shortcuts import render

# Create your views here.

# Create your views here.
from .models import Product
import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from .form import FormProductForm
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

"""class ProductList(APIView):
    def get(self, request):
        Product1=Product.objects.all()
        serializer=ProductSerializer(Product1,many=True)
        return Response(serializer.data)"""




class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset =Product.objects.all()

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None ):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)


    def post(self, request):
        return self.list(request)

    def put(self, request,  id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):
    if request.method == 'GET':
        try:
            Products = FormProductForm.objects.all()
            Product_serializer = ProductSerializer(Products, many=True)

            response = {
                'message': "Get all Products'Infos Successfully",
                'products': Product_serializer.data,
                'error': ""
            }
            return Response(Product_serializer.data)

        except:
            error = {
                'message': "Fail! -> can NOT get all the customers List. Please check again!",
                'customers': "[]",
                'error': "Error"
            }
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            product_data = JSONParser().parse(request)
            product_serializer = ProductSerializer(data=product_data)
            if product_serializer.is_valid():
                product_serializer.save()
                print(product_serializer.data)
                response = {
                    'message': "Successfully Upload a ProductForm with id = %d" % product_serializer.data.get('id'),
                    'products': [product_serializer.data],
                    'error': ""
                }
                return Response(response, status=status.HTTP_201_CREATED)

            else:
                error = {
                    'message': "Can Not upload successfully!",
                    'products': "[]",
                    'error': product_serializer.errors
                }
                return Response(error, status=status.HTTP_400_BAD_REQUEST)

        except:
            exceptionError = {
                'message': "Can Not upload successfully!",
                'products': "[]",
                'error': "Having an exception!"
            }
            return Response(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR);

    elif request.method == 'DELETE':
        try:
            FormProductForm.objects.all().delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        except:
            exceptionError = {
                'message': "Can Not Deleted successfully!",
                'products': "[]",
                'error': "Having an exception!"
            }
            return Response(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR);

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product= Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        exceptionError = {
            'message': "Not found a Product with id = %s!" % pk,
            'products': "[]",
            'error': "404 Code - Not Found!"
        }
        return Response(exceptionError, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        product_serializer = ProductSerializer(product)
        response = {
            'message': "Successfully get a ProductForm with id = %s" % pk,
            'products': [product_serializer.data],
        }
        return Response(response, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            product_serializer= ProductSerializer(Product, data=request.data)

            if product_serializer.is_valid():
                product_serializer.save()
                response = {
                    'message': "Successfully Update a ContactForm with id = %s" % pk,
                    'products': [product_serializer.data],
                    'error': ""
                }
                return Response(response, status=status.HTTP_201_CREATED)
            response = {
                'message': "Fail to Update a Customer with id = %s" % pk,
                'products': [product_serializer.data],
                'error': product_serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except:
            exceptionError = {
                'message': "Fail to update a ProductForm with id = %s!" % pk,
                'products': [product_serializer.data],
                'error': "Internal Error!"
            }
            return Response(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        print("Deleting a ProductForm with id=%s" % pk)
        Product.delete()
        product_serializer = ProductSerializer(product)
        response = {
            'message': "Successfully Delete a Customer with id = %s" % pk,
            'products': [product_serializer.data],
            'error': ""
        }
        return Response(response,status=status.HTTP_204_NO_CONTENT)





#Login
def Product1(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/AddProduct.html', context)

def ProductHome(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/ProductHome.html', context)
"""def orderidseller(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/orderidseller.html', context)"""
"""def sellerorder(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/sellerorder.html', context)"""
"""def vieworderidseller(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/orderidseller.html', context)"""
"""def Buyer(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/buyer.html', context)"""

"""def orderidbuyer(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/orderidbuyer.html', context)"""

"""def seller(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/seller.html', context)"""
"""def sellerprofile(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/sellerprofile.html', context)"""
"""def buyerprofile(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/buyerprofile.html', context)"""

def Dashboard(request):
    if request.method=="POST":
        form = FormProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=FormProductForm()

    context = {'form': form}

    return render(request, 'Product/Dashboard.html', context)



