Year of the Snake in Hong Kong
=====================

During my trip, I took a lot of photos, and I have created a [photo gallery](http://homing-hkphotos.stacka.to/) for my Instagram Hong Kong pictures. The stack you ask? uwsgi, Python, Django, and I included both the [TN3](http://www.tn3gallery.com/) and [galleria](http://galleria.io/) javascript for the photo gallery, all running on [Stackato](http://www.activestate.com/stackato).

Step-by-step:

    git clone git://github.com/homingli/homing-hkphotos.git
    cd homing-hkphotos
    stackato target <api-endpoint>
    stackato login
    stackato push -n

Built on https://github.com/pinax/pinax-project-account
