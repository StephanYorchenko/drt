class AnnouncementFilter:
    pass


class RequestFilter:
    pass


class Filter(AnnouncementFilter, RequestFilter):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
