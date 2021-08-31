import arrow

utc = arrow.utcnow()
print(utc.to('local'))

dt = arrow.now()
print(dt)
print(dt.to('utc'))
print(dt.timestamp())

print(arrow.get('2021-08-31 21:52:17', 'YYYY-MM-DD HH:mm:ss'))


import json

payload = {
    'key2': 'value1',
    'key1': ['v1', 'v2'],
}

print(json.dumps(payload, sort_keys=True, indent=4))
