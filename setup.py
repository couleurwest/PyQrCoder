from setuptools import setup

setup(
    name= "PyQrCoder",
    version='1.0.0',
    packages=['wwwproject'],

    setup_requires=['libsass >= 0.21.0'],
    sass_manifests={'.': ('wwwproject/sass', 'wwwproject/xwork', 'wwwproject/css')}

)

#python -m eel [your_main_script] [your_web_folder]
#pyinstaller main.py --hidden-import bottle_websocket --add-data C:\Python310\lib\site-packages\eel\eel.js;eel --add-data wwwproject;wwwproject --onefile --noconsole


"""
Copyright fonts : <div>Font made from <a href="http://www.onlinewebfonts.com">oNline a11y-atkinson</a>is licensed by CC BY 3.0</div>
 Copyright (c) 2011 by Santiago Orozco (hi@typemade.mx) with reserved name Italiana 
"""