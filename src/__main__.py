from src.wrappers import patch_notes as pn, \
                         platform as pl

#print(pn.get_patch_notes().display_api_obj())

#print(pl.get_achievements('eldrad-2799','pc','eu').display_api_obj())

#print(pl.get_platforms('eldrad-2799','pc','eu')[0].display_api_obj())

print(pl.get_profile('eldrad-2799','pc','eu').display_api_obj())