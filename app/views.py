from django.views.generic import TemplateView
from .models import Image


class ImageBoard(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        images = Image.objects.all()

        context = {
            'images': images
        }

        return context
