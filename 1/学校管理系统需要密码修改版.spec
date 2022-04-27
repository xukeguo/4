# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
file = [
        '学校管理系统需要密码修改版.py',
        '教师信息录入系统teacher.py',
        '学生信息录入系统student..py'
        ]

a = Analysis(,
    pathex=['/Users/xkg/Library/CloudStorage/OneDrive-个人/python/4/学校管理 系统student\&teacher'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='学校管理系统需要密码修改版',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='学校管理系统需要密码修改版',
)
