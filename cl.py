import serial, sys, time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from yolo import check,send
# Fetch the service account key JSON file contents
cred = credentials.Certificate('smart-inventory.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-inventory-f9955-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('/')
start = 0
end = 0

while True:
    if(check):
        current_ref = ref
        msg = send()
        current_ref.set(msg)


# with serial.Serial(port=sys.argv[1], baudrate=sys.argv[2]) as ser:
#     while ser.isOpen():
#         end = time.time()
#         current_data = ser.readline()
#         for a_byte in current_data:
#             a_byte = a_byte - 48
#             if end - start >= 5:
#                 print(a_byte)
#                 current_ref = ref
#                 current_ref.set(a_byte)
#                 start = end
#             break
