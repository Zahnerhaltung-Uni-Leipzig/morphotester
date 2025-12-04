# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules, collect_data_files, copy_metadata

# Collect all submodules for traitsui and pyface Qt backends
hiddenimports = collect_submodules('traitsui.qt')
hiddenimports += collect_submodules('pyface.qt')
hiddenimports += collect_submodules('pyface.ui.qt')
hiddenimports += collect_submodules('pyface.timer')
hiddenimports += collect_submodules('tvtk')
hiddenimports += collect_submodules('mayavi')

# Collect entry points metadata
datas = copy_metadata('traitsui')
datas += copy_metadata('pyface')
datas += copy_metadata('mayavi')
datas += copy_metadata('traits')

# Collect tvtk_classes data files (required for TVTK to work)
datas += collect_data_files('tvtk')

a = Analysis(
    ['Morpho.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports + [
        # Local modules
        'topomesh',
        'plython',
        'DNE',
        'OPC',
        'RFI',
        'implicitfair',
        'normcore',
        'render',
        # VTK
        'vtkmodules',
        'vtkmodules.all',
        # PyQt5
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Morpho',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Morpho',
)
