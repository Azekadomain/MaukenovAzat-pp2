import json
with open(r'C:\Users\User\Desktop\PP2\LAB4\data.json') as file:
    data = json.load(file)

print('Interface Status')
print('='*80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
for entry in data['imdata']:
    attributes = entry.get('l1PhysIf', {}).get('attributes', {})
    dn = attributes.get('dn', '')
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))