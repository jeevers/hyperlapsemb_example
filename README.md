HYPERLAPSEMB_EXAMPLE
====================

Simple webapp that serves out the HyperlapseMB examples.

I had trouble running the examples straight from the desktop, so I got tornado to serve it out from the static directory. The HyperlapseMB git repository can be found here:

https://github.com/proog128/HyperlapseMB


Python requirements:
--------------------
Tornado

Setup:
------
1. (Optional) Configure a virtualenv:
    
    virtualenv hyperlapse_example
   
2. (Optional) Activate the virtualenv:
    
    cd hyperlapse_example
    . bin/activate
    
3. Install the required python modules
    
    pip install -r requirements.txt
    
4. Start the application
    
    cd hyperlapse_example
    python boilerplate.py

The simple and viewer examples can be accessed from:

http://localhost:8800/static/simple.html
http://localhost:8800/static/viewer.html

