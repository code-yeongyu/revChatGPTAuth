from enum import Enum


class SupportedBrowser(Enum):
    '''Supported browsers for cookie extraction.'''
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    OPERA = 'opera'
    OPERA_GX = 'opera gx'
    EDGE = 'edge'
    CHROMIUM = 'chromium'
    BRAVE = 'brave'
    VIVALDI = 'vivaldi'
    SAFARI = 'safari'
