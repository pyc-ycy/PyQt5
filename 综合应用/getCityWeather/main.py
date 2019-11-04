# -*- mode: python -*-
from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis

block_cipher = None

a = Analysis(['main.py', 'monitor.py',
              'D:\\users\lenovo\PyQt5\综合应用\getCityWeather\CallWeatherWin.py',
              'D:\\users\lenovo\PyQt5\综合应用\getCityWeather\WeatherWin.py',
              'D:\\users\lenovo\PyQt5\综合应用\getCityWeather\images_rc.py'],
             pathex=['test_wpf_python_msg'],
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
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
