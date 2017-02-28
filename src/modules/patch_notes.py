from src.contracts.api_contract import APIContract
from utils import html_stripper as hs
#
class PatchNotes(APIContract):
    #
    def __init__(self, program, locale, type, patch_version, status, detail, build_number, publish, created, updated,
                 develop, slug, version):
        self.program = hs.html_stripper(program)
        self.locale = hs.html_stripper(locale)
        self.type = hs.html_stripper(type)
        self.patch_version = hs.html_stripper(patch_version)
        self.status = hs.html_stripper(status)
        self.detail = hs.html_stripper(detail)
        self.build_number = hs.html_stripper(build_number)
        self.publish = hs.html_stripper(publish)
        self.created = hs.html_stripper(created)
        self.updated = hs.html_stripper(updated)
        self.develop = hs.html_stripper(develop)
        self.slug = hs.html_stripper(slug)
        self.version = hs.html_stripper(version)
    #
    def display_api_obj(self):
        print("Program: ", self.program,
              "\nLocale: ", self.locale,
              "\nType: ", self.type,
              "\nPatch Version: ", self.patch_version,
              "\nStatus: ", self.status,
              "\nDetail: ", self.detail,
              "\nBuild Number: ", self.build_number,
              "\nPublish: ", self.publish,
              "\nCreated: ", self.created,
              "\nUpdated: ", self.updated,
              "\nDevelop: ", self.develop,
              "\nSlug: ", self.slug,
              "\nVersion: ", self.version,
              "\n------------------------------------------")