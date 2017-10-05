class clubbeamer():
    set = {
        'on': b'* 0 IR 001\r',
        'off': b'* 0 IR 002\r',
        'vga': b'* 0 IR 015\r',
        'hdmi1': [b'* 0 IR 015\r', b'* 0 IR 050\r'],
        'hdmi2': [b'* 0 IR 015\r', b'* 0 IR 050\r', b'* 0 IR 050\r']
    }
    get = {
        'state': [b'* 0 Lamp ?\r', r'.*Lamp.1.*']
    }
