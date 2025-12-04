# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Morpho.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[
        # Local modules
        'topomesh',
        'plython',
        'DNE',
        'OPC',
        'RFI',
        'implicitfair',
        'normcore',
        'render',
        # TraitsUI Qt toolkit
        'traitsui.qt',
        'traitsui.qt.api',
        'pyface.qt',
        'pyface.qt.api',
        'pyface.ui.qt',
        'pyface.ui.qt.api',
        # Mayavi
        'mayavi',
        'mayavi.core.ui.api',
        'tvtk.pyface.scene_editor',
        'tvtk.pyface.api',
        'tvtk.api',
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
    a.binaries,
    a.datas,
    [],
    name='Morpho',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
