from time import time

import pdfkit
from django.core.files.base import ContentFile

from intelsAPI.models import IntelFile


class Bookmarker:
    @staticmethod
    def assert_valid_filename(filename):
        valid = len(filename) > 0 and filename[-4:] == ".pdf"
        if not valid:
            raise NameError

    @staticmethod
    def get_default_filename():
        time_info = int(time())
        return f"snapshot_{time_info}.pdf"

    @staticmethod
    def create_snapshot(intel, filename=None, save=True):
        assert intel.link

        if filename is None:
            filename = Bookmarker.get_default_filename()
        Bookmarker.assert_valid_filename(filename)

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
