from src.contracts.api_contract import APIContract
#
class PatchNotes(APIContract):
    #
    def __init__(self, program, locale, type, patch_version, status, detail, build_number, publish, created, updated,
                 develop, slug, version):
        self.program = program
        self.locale = locale
        self.type = type
        self.patch_version = patch_version
        self.status = status
        self.detail = detail
        self.build_number = build_number
        self.publish = publish
        self.created = created
        self.updated = updated
        self.develop = develop
        self.slug = slug
        self.version = version
    #
    def display_api_obj(self):
        print("Program: " + self.program +
              "\nLocale: " + self.locale +
              "\nType: " + self.type +
              "\nPatch Version: " + self.patch_version +
              "\nStatus: " + self.status +
              "\nDetail: " + self.detail +
              "\nBuild Number: " + self.build_number +
              "\nPublish: " + self.publish +
              "\nCreated: " + self.created +
              "\nUpdated: " + self.updated +
              "\nDevelop: " + self.develop +
              "\nSlug: " + self.slug +
              "\nVersion: " + self.version)