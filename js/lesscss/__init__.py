from fanstatic import Library, Resource

library = Library('less', 'resources')

lesscss_js = Resource(library, 'less.min.js')
lesscss = lesscss_js
