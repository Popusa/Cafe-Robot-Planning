requested_coffee = [[],[],[],[],[]]
success_state = False
path = []
env = [
['-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','0','TA10','TA9','0','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','0','TA11','TA8','0','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','0','0','0','TA7','-1','-1','-1','-1','-1','-1',],
['-1','-1','-1','-1','TA13','TA12','0','TA15','TA14','0','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','0','0','0','TA17','TA16','0','TA6','-1','-1','-1','-1','-1'],
['-1','-1','-1','0','0','0','0','TA19','TA18','0','0','0','TA5','-1','-1','-1'],
['-1','-1','-1','-1','-1','0','0','TA21','TA20','0','0','0','TA4','-1','-1','-1'],
['-1','-1','-1','-1','-1','0','0','0','0','0','0','0','0','-1','-1','-1'],
['-1','-1','DR','ES','-1','-1','DW3','-1','-1','-1','0','0','TA3','-1','-1','-1'],
['-1','-1','0','0','DW2','0','0','0','0','-1','0','0','TA2','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','-1','0','0','0','DW4','0','TA1','-1','-1','-1'],
['-1','-1','0','0','CR','0','DW1','0','0','-1','-1','-1','-1','-1','-1','-1'],
['-1','-1','0','0','CM','0','-1','0','0','-1','-1','-1','-1','-1','-1','-1'],
['-1','-1','0','0','0','0','-1','0','0','-1','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1'],
]
mapped_name = [
['-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','0','TA10','TA9','0','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','0','TA11','TA8','0','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','0','0','0','TA7','-1','-1','-1','-1','-1','-1',],
['-1','-1','-1','-1','TA13','TA12','0','TA15','TA14','0','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','0','0','0','TA17','TA16','0','TA6','-1','-1','-1','-1','-1'],
['-1','-1','-1','0','0','0','0','TA19','TA18','0','0','0','TA5','-1','-1','-1'],
['-1','-1','-1','-1','-1','0','0','TA21','TA20','0','0','0','TA4','-1','-1','-1'],
['-1','-1','-1','-1','-1','0','0','0','0','0','0','0','0','-1','-1','-1'],
['-1','-1','DR','ES','-1','-1','DW3','-1','-1','-1','0','0','TA3','-1','-1','-1'],
['-1','-1','0','0','DW2','0','0','0','0','-1','0','0','TA2','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','-1','0','0','0','DW4','0','TA1','-1','-1','-1'],
['-1','-1','0','0','CR','0','DW1','0','0','-1','-1','-1','-1','-1','-1','-1'],
['-1','-1','0','0','CM','0','-1','0','0','-1','-1','-1','-1','-1','-1','-1'],
['-1','-1','0','0','0','0','-1','0','0','-1','-1','-1','-1','-1','-1','-1'],
['-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1'],
]
door_stat = [
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW',],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW',False,'NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW',False,'NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW',False,'NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','CR','NDW',False,'NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','CM','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
['NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW','NDW'],
]