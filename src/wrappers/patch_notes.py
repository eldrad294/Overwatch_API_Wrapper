from urllib.request import urlopen
import urllib
import src.constants as const
import json
from src.modules import patch_notes as pn
#
def get_patch_notes():
    #
    try:
        patch_notes = json.load(const.codec(urlopen(const.URL + "patch_notes")))
        result = pn.PatchNotes(patch_notes['patchNotes'][0]['program'],
                               patch_notes['patchNotes'][0]['locale'],
                               patch_notes['patchNotes'][0]['type'],
                               patch_notes['patchNotes'][0]['patchVersion'],
                               patch_notes['patchNotes'][0]['status'],
                               patch_notes['patchNotes'][0]['detail'],
                               patch_notes['patchNotes'][0]['buildNumber'],
                               patch_notes['patchNotes'][0]['publish'],
                               patch_notes['patchNotes'][0]['created'],
                               patch_notes['patchNotes'][0]['updated'],
                               patch_notes['patchNotes'][0]['develop'],
                               patch_notes['patchNotes'][0]['slug'],
                               patch_notes['patchNotes'][0]['version'])
        return result
    except urllib.error.URLError as e:
        print("An error occurred when fetching stats\n" + e)