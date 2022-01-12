
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee

class BaseView(APIView):
    def get(self,request):
        result_data=[]
        qs=Employee.objects.all()
        for i in qs:
            data={}
            data['eno']=object.id
            result_data.append(data)


        return Response({'Status':True,'result_data':result_data})



    # order_field = None
    # """
    # Returns JSON or HTML representations of "new" definitions.
    # """
    # renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    # def get(self, request):

    #     # Queryset
    #     definitions = Definition.objects.filter(language=get_language())
    #     definitions = definitions.order_by(self.order_field)

    #     # HTML
    #     if request.accepted_renderer.format == "html":
    #         context = {}
    #         context["definitions"] = definitions
    #         context["tags"] = get_tags(definitions)
    #         return Response(context, template_name="dictionary/index.html")

    #     # JSON
    #     serializer = DefinitionSerializer(definitions, many=True)
    #     return Response(serializer.data)