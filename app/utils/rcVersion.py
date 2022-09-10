import json
import os.path
import os
from datetime import date 


today = date.today()
releaseDate = today.strftime("%d/%m/%Y")
package_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'package.json'))

print(':::reading current package.json')
current_package = open(package_path)

print(':::opening json data')
data = json.load(current_package)
current_version = data['version']

print (':::updating rc version')
data['version'] = current_version + '-rc.' + os.environ.get('BITRISE_BUILD_NUMBER')
data['build'] = os.environ.get('BITRISE_BUILD_NUMBER')
data['releaseDate'] = releaseDate

updatedPackageJSON = json.dumps(data, indent=2)

with open(package_path, 'w') as outfile:
    outfile.write(updatedPackageJSON)

print(':::pacakage.json was updated')
