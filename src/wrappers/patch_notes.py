import json
import urllib
from urllib.request import urlopen
import src.constants as const
from src.modules import patch_notes as pn


#
def get_patch_notes():
    """ API wrapper method which returns a list of patch noteobjects """
    #
    patch_note_list =[]
    try:
        patch_notes = json.load(const.codec(urlopen(const.URL + "patch_notes")))
        for patch_note in patch_notes['patchNotes']:
            result = pn.PatchNotes(patch_note['program'],
                                   patch_note['locale'],
                                   patch_note['type'],
                                   patch_note['patchVersion'],
                                   patch_note['status'],
                                   patch_note['detail'],
                                   patch_note['buildNumber'],
                                   patch_note['publish'],
                                   patch_note['created'],
                                   patch_note['updated'],
                                   patch_note['develop'],
                                   patch_note['slug'],
                                   patch_note['version'])
            patch_note_list.append(result)
        return patch_note_list
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + str(e))
        exit(1)
    except Exception as e:
        print("An error occurred:\n " + str(e))
        exit(1)