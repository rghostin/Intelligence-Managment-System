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
    def create_snapshot(intel, link, filename=None):
        """
        Given an intel and a link, create a
        corresponding intelfile as a pdf snapshot of the webpage
        :param intel: the intel to snapshot
        :param link: like of the page to bookmark
        :param filename:
        :return: The created IntelFile instance
        """

        if filename is None:
            filename = Bookmarker.get_default_filename()
        else:
            if filename[-4:0] != ".pdf":
                filename += ".pdf"
        Bookmarker.assert_valid_filename(filename)

        # download snapshot
        options = {
            'quiet': ''
        }
        pdf_data = pdfkit.from_url(link, False, options=options)

        # create intelFile
        pdf_file_content = ContentFile(pdf_data)
        intelfile = IntelFile(intel=intel, link=link)
        intelfile.file.save(filename, pdf_file_content)
        intelfile.save()

        return intelfile
