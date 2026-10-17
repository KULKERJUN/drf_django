from api_app.models import *
from api_app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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

#single get update delete

@api_view(['GET','PUT','DELETE'])
def product_detail_view(request, p_id):
     if request.method == 'GET':
        try:
           data = ProductModel.objects.get(id=p_id)
        except:
             return Response({
                  'success':False,
                  'message':'Data getting is unsuccessful',
                  'data':[]
             },status = status.HTTP_404_NOT_FOUND)
        
        serializers_data = ProductSerializer(data)
        return Response({
                  'success':True,
                  'message':'Data getting is successful',
                  'data': serializers_data.data
             },status = status.HTTP_200_OK)

     if request.method == 'DELETE':
             try:
                data = ProductModel.objects.get(id=p_id)
             except:
                  return Response({
                       'success':False,
                       'message':'Data deleting is unsuccessful',
                       'data':[]
                  },status = status.HTTP_404_NOT_FOUND)
             
             data.delete()
             return Response({
                       'success':True,
                       'message':'Data deleting is successful',
                       'data': serializers_data.data
                  },status = status.HTTP_200_OK)