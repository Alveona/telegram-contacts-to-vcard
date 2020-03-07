import vobject
import json

FILE_NAME_IN = 'example.json'
FILE_NAME_OUT = 'example.vcf'

_input = json.load(open(FILE_NAME_IN, encoding='utf-8')) # to support unicode emojis

contacts = dict() # hashmap will drop any duplicates, we use full_name as a key
for contact in _input['contacts']['list']:
    full_name = contact['first_name'] + (' ' if contact['last_name'] else '') + contact['last_name']
    info = {
        "phone_number": contact['phone_number'],
        "first_name": contact['first_name'],
        "last_name": contact['last_name']
    }
    if info['phone_number'][0] == '0' and info['phone_number'][1] == '0': # in some random contacts tg interprets '+' as '00', so we fix it
        info['phone_number'] = '+' + info['phone_number'][2:] 
    contacts[full_name] = info
    
print(f'Found {len(contacts)} unique contacts') # intermediate result

_output = ''
for name, info in contacts.items():
    card = vobject.vCard()
    card.add('n').value = vobject.vcard.Name(family=info['last_name'], given=info['first_name'])
    card.add('fn').value = name
    card.add('tel').value = info['phone_number']
    _output += card.serialize()    
    _output += '\n'

file = open(FILE_NAME_OUT, 'w+')
file.write(_output)
file.close()

print('Sucessfully exported to .vcf')