import json
#dumps --- dict to string
#loads --- string to dict
key= {
    "status": True,
    "RFID_MAC_ADDRESS": "C0:94:B0:39:56:60",
    "REMOVE_LEADING_ZERO": True
}

with open('config_1.json','r') as json_fd:
    json_data=json_fd.read()
    json_data_dict=json.loads(json_data)
    print(json_data_dict)
    json_fd.close()

print(json_data_dict['dev']['rfid'])

#logic???
json_data_dict['dev']['rfid']['status']=key['status']
json_data_dict['dev']['rfid']['RFID_MAC_ADDRESS']=key['RFID_MAC_ADDRESS']
json_data_dict['dev']['rfid']['SCANNED_DATA_CONF']['REMOVE_LEADING_ZERO']=key['REMOVE_LEADING_ZERO']
with open('config_1_spare.json','w') as json_fd:
    data=json.dumps(json_data_dict)
    json_fd.write(data)
    json_fd.close()

'''import os
os_dir=os.listdir()
for file_js in os_dir:
    if(file_js.spit('.')[-1]=='json'):
        print(file_js)'''



