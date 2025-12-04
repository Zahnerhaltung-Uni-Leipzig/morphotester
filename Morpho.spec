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

# Collect all data files for ETS packages
datas += collect_data_files('tvtk')
datas += collect_data_files('mayavi')
datas += collect_data_files('pyface')
datas += collect_data_files('traitsui')

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
        'vtkmodules.util',
        'vtkmodules.util.colors',
        'vtkmodules.util.numpy_support',
        'vtkmodules.numpy_interface',
        'vtkmodules.numpy_interface.algorithms',
        'vtkmodules.numpy_interface.dataset_adapter',
        # NumPy internals (needed by apptools persistence)
        'numpy.core.multiarray',
        'numpy.core._multiarray_umath',
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
    console=True,  # Temporarily enable for debugging
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
