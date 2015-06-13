class TextOutput(object):  # TODO some parent class to do what...?

    def __init__(self, fd, collector):
        self.fd = fd
        self.collector = collector

    def dump(self):
        self.fd.write("""
DueCredit Report

%d pieces were cited:
        """ % len(self.collector.citations))
        # Group by type???? e.g. Donations should have different meaning from regular ones
        # Should we provide some base classes to differentiate between types? probbly not -- tags?


