import json
import os.path
import os

package_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'package.json'))

print(':::reading current package.json')
current_package = open(package_path)

print(':::opening json data')
data = json.load(current_package)
current_version = data['version']

print (':::updating rc version')
data['version'] = current_version + '-rc.' + os.environ.get('BITRISE_BUILD_NUMBER')

print(data)

# package_data = json.load(current_package)