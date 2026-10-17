from api_app.models import *
from api_app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        product_data = ProductModel.objects.all()
        serializers = ProductSerializer(product_data, many = True)
        return Response(serializers.data)

    if request.method == 'POST':
            serializers = ProductSerializer(data = request.data)
            if serializers.is_valid():
                 serializers.save()
            return Response({
                 'success': True,
                 'message': 'Product Created Successfully',
                 'data': serializers.data
            })