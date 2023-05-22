from imagescanner import ImageScanner

# instantiate the imagescanner obj
iscanner = ImageScanner()

# get all available devices
scanners = iscanner.list_scanners()

# choose one of the devices
scanner = scanners[0]

# scan your file (returns a PIL object)
scanner.scan()