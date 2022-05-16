from configparser import ConfigParser, ExtendedInterpolation

parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.read('extended_interpolation.ini')

print('Original value:', parser.get('bug_tracker', 'url'))
parser.set('intranet', 'port', '9090')
print('Altered port value:', parser.get('bug_tracker', 'url'))

print('Without interpolation:', parser.get('bug_tracker', 'url', raw=True))
