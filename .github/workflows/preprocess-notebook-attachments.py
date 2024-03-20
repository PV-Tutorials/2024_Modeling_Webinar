# from https://github.com/executablebooks/jupyter-book/issues/1087#issuecomment-1969119486

import base64
import json
import glob

filenames = glob.glob('*ipynb')

for fn in filenames:
    with open(fn) as f:
        nb = json.load(f)
    
    attachments = [cell.get('attachments') for cell in nb['cells']]
    attachments = [a for a in attachments if a]
    
    for attachment in attachments:
        for name, data in attachment.items():
            for filetype, encoded in data.items():
                print(f'{name} ({filetype})')
                img_data = base64.b64decode(encoded)
                with open(f'attachment:{name}', 'wb') as img:
                    img.write(img_data)
