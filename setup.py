from setuptools import setup

setup(
    name= "PyQrCoder",
    version='1.0.0',
    packages=['wwwproject'],

    setup_requires=['libsass >= 0.21.0'],
    sass_manifests={'.': ('wwwproject/sass', 'wwwproject/xwork', 'wwwproject/css')}

)

#python -m eel [your_main_script] [your_web_folder]
#wine python -m eel main.py wwwproject -n PyQrCoder  --add-data="config.yml;." --add-data="main.js;." --add-data="package.json;." --clean --noconfirm -i "wwwproject/logo.ico" --hidden-import bottle_websocket --noconsole  --windowed
