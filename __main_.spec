# -*- mode: python -*-

block_cipher = None


a = Analysis(['src\\__main_.py'],
             pathex=['D:\\Projects\\Overwatch_API_Wrapper'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='__main_',
          debug=False,
          strip=False,
          upx=True,
          console=True )