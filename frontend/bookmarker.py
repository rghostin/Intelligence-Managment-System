import pdfkit
from django.core.files.base import ContentFile

from intelsAPI.models import IntelFile


class Bookmarker:
    @staticmethod
    def is_valid_filename(filename):
        return len(filename) > 0

    @staticmethod
    def create_snapshot(intel, filename="snapshot", save=True):
        if not Bookmarker.is_valid_filename(filename):
            raise NameError
        filename = filename + ".pdf"

        # download snapshot
        options = {
            'quiet': ''
        }
        pdf_data = pdfkit.from_url(intel.link, False, options=options)

        # create intelFile
        pdf_file_content = ContentFile(pdf_data)
        intelfile = IntelFile(intel=intel)
        print(filename)
        intelfile.file.save(filename, pdf_file_content)

        if save:
            intelfile.save()

        return intelfile
