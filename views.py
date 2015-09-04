from rest_framework.decorators import detail_route, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class UpdateUploadMixin(object):
    upload_fields = []

    def __init__(self, *args, **kwargs):
        super(UpdateUploadMixin, self).__init__(*args, **kwargs)

    @detail_route(methods=['POST'], permission_classes=[IsAuthenticated])
    @parser_classes((FormParser, MultiPartParser,))
    def file(self, request, pk):
        for upload in self.upload_fields:
            if upload in request.FILES:
                instance = self.get_object()

                getattr(instance, upload)

                instance.__dict__[upload].delete()

                upload_data = request.data[upload]

                instance.__dict__[upload].save(upload_data.name, upload_data)

                return Response(instance.__dict__[upload].url, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)

    @detail_route(methods=['POST'], permission_classes=[IsAuthenticated])
    @parser_classes((FormParser, MultiPartParser,))
    def image(self, request, pk):
        return self.file(request, pk)
