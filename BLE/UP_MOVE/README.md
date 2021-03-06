
## Scratch Notes
Found :https://github.com/matianfu/jawbone-droid/blob/master/src/com/example/android/bluetoothlegatt/SampleGattAttributes.java

``` Local Device
DB:CB:F9:AB:FD:5D UP MOVE
```

####  Characteristics
```Characteristics

handle: 0x0002, char properties: 0x0e, char value handle: 0x0003, uuid: 00002a00-0000-1000-8000-00805f9b34fb
handle: 0x0004, char properties: 0x02, char value handle: 0x0005, uuid: 00002a01-0000-1000-8000-00805f9b34fb
handle: 0x0006, char properties: 0x02, char value handle: 0x0007, uuid: 00002a04-0000-1000-8000-00805f9b34fb
handle: 0x000a, char properties: 0x18, char value handle: 0x000b, uuid: f7c9b162-6658-4390-b53c-1de5e1453654
handle: 0x000d, char properties: 0x10, char value handle: 0x000e, uuid: f7c9ba82-6658-4390-b53c-1de5e1453654
handle: 0x0010, char properties: 0x10, char value handle: 0x0011, uuid: f7c9ba91-6658-4390-b53c-1de5e1453654
handle: 0x0014, char properties: 0x02, char value handle: 0x0015, uuid: 00002a29-0000-1000-8000-00805f9b34fb
handle: 0x0017, char properties: 0x02, char value handle: 0x0018, uuid: 00002a26-0000-1000-8000-00805f9b34fb
handle: 0x001a, char properties: 0x02, char value handle: 0x001b, uuid: 00002a24-0000-1000-8000-00805f9b34fb
handle: 0x001d, char properties: 0x02, char value handle: 0x001e, uuid: 00002a28-0000-1000-8000-00805f9b34fb
handle: 0x0020, char properties: 0x02, char value handle: 0x0021, uuid: 00002a27-0000-1000-8000-00805f9b34fb

```

#### Char Desc
```
[DB:CB:F9:AB:FD:5D][LE]> char-desc
handle: 0x0001, uuid: 00002800-0000-1000-8000-00805f9b34fb
handle: 0x0002, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0003, uuid: 00002a00-0000-1000-8000-00805f9b34fb
handle: 0x0004, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0005, uuid: 00002a01-0000-1000-8000-00805f9b34fb
handle: 0x0006, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0007, uuid: 00002a04-0000-1000-8000-00805f9b34fb
handle: 0x0008, uuid: 00002800-0000-1000-8000-00805f9b34fb
handle: 0x0009, uuid: 00002800-0000-1000-8000-00805f9b34fb
handle: 0x000a, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x000b, uuid: f7c9b162-6658-4390-b53c-1de5e1453654
handle: 0x000c, uuid: 00002902-0000-1000-8000-00805f9b34fb
handle: 0x000d, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x000e, uuid: f7c9ba82-6658-4390-b53c-1de5e1453654
handle: 0x000f, uuid: 00002902-0000-1000-8000-00805f9b34fb
handle: 0x0010, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0011, uuid: f7c9ba91-6658-4390-b53c-1de5e1453654
handle: 0x0012, uuid: 00002902-0000-1000-8000-00805f9b34fb
handle: 0x0013, uuid: 00002800-0000-1000-8000-00805f9b34fb
handle: 0x0014, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0015, uuid: 00002a29-0000-1000-8000-00805f9b34fb
handle: 0x0016, uuid: 00002904-0000-1000-8000-00805f9b34fb
handle: 0x0017, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0018, uuid: 00002a26-0000-1000-8000-00805f9b34fb
handle: 0x0019, uuid: 00002904-0000-1000-8000-00805f9b34fb
handle: 0x001a, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x001b, uuid: 00002a24-0000-1000-8000-00805f9b34fb
handle: 0x001c, uuid: 00002904-0000-1000-8000-00805f9b34fb
handle: 0x001d, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x001e, uuid: 00002a28-0000-1000-8000-00805f9b34fb
handle: 0x001f, uuid: 00002904-0000-1000-8000-00805f9b34fb
handle: 0x0020, uuid: 00002803-0000-1000-8000-00805f9b34fb
handle: 0x0021, uuid: 00002a27-0000-1000-8000-00805f9b34fb
handle: 0x0022, uuid: 00002904-0000-1000-8000-00805f9b34fb

```



| UUID                                 | Value                    | Value(ASCII)  | Assessment    |
| ------------------------------------ |:------------------------:| -------------:| -------------:|
| 00002a01-0000-1000-8000-00805f9b34fb | 55 50 20 4d 4f 56 45     | UP MOVE       | Appearance    |
| 00002a04-0000-1000-8000-00805f9b34fb | ff ff ff ff 07 00 ff ff  |               | Peripheral Pref Connection Parameters              |
| f7c9b162-6658-4390-b53c-1de5e1453654 |                          |               |               |
| f7c9ba82-6658-4390-b53c-1de5e1453654 |                          |               |               |
| f7c9ba91-6658-4390-b53c-1de5e1453654 |                          |               |               |
| 00002a29-0000-1000-8000-00805f9b34fb | 4a 61 77 62 6f 6e 65 00  | Jawbone       | Manufacturer Name String              |
| 00002a26-0000-1000-8000-00805f9b34fb | 34 2e 30 2e 32 37        | 4.0.27        | Firmware Revision String              |
| 00002a24-0000-1000-8000-00805f9b34fb | 55 50 20 4d 6f 76 65 00  | UP Move       | Model Number String              |
| 00002a28-0000-1000-8000-00805f9b34fb | 34 2e 30 2e 32 37        | 4.0.27        | Software Revision String               |
| 00002a27-0000-1000-8000-00805f9b34fb | 31 34                    | 14            | Hardware Revision String              |
| 00002902-0000-1000-8000-00805f9b34fb |                          |               | Client Characteristic Configuration |
| 00002904-0000-1000-8000-00805f9b34fb |                          |               | Characteristic Presentation Format |



(Walked around for couple hours and retested)


Data dumping:

| UUID      | Value (HEX)                   | Value(ASCII) | Assessment    |
| --------- |:-----------------------------:| ------------:| -------------:|
|  0x0001   | 00 18                         | ..           |               |
|  0x0008   | 01 18                         | ..           |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x0003   | 55 50 20 4d 4f 56 45          | UP MOVE      | Device Name?  |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x0005   | 00 00                         | ..           |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x0007   | ff ff ff ff 07 00 ff ff       | ........     |               |
|  0x0001   | 00 18                         | ..           |               |
|  0x0008   | 01 18                         | ..           |               |
|  0x0001   | 00 18                         | ..           |               |
|  0x0008   | 01 18                         | ..           |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x000c   | 00 00                         | ..           |               |
|  0x000f   | 00 00                         | ..           |               |
|  0x0012   | 00 00                         | ..           |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x000c   | 00 00                         | ..           |               |
|  0x000f   | 00 00                         | ..           |               |
|  0x0012   | 00 00                         | ..           |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x000c   | 00 00                         | ..           |               |
|  0x000f   | 00 00                         | ..           |               |
|  0x0012   | 00 00                         | ..           |               |
|  0x0001   | 00 18                         | ..           |               |
|  0x0008   | 01 18                         | ..           |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x0015   | 4a 61 77 62 6f 6e 65 00       | Jawbone.     |               |
|  0x0016   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0019   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x0018   | 34 2e 30 2e 32 37             | 4.0.27       |               |
|  0x0016   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0019   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x001b   | 55 50 20 4d 6f 76 65 00       | UP Move.     |               |
|  0x0016   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0019   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x001e   | 34 2e 30 2e 32 37             | 4.0.27       |               |
|  0x0016   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0019   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0002   | 0e 03 00 00 2a                | ....*        |               |
|  0x0004   | 02 05 00 01 2a                | ....*        |               |
|  0x0006   | 02 07 00 04 2a                | ....*        |               |
|  0x0021   | 31 34                         | 14           |               |
|  0x0016   | 19 00 00 00 01 00 00          | .......      |               |
|  0x0019   | 19 00 00 00 01 00 00          | .......      |               |




Found :https://github.com/matianfu/jawbone-droid/blob/master/src/com/example/android/bluetoothlegatt/SampleGattAttributes.java

| UUID                                 | Description                            |
| ------------------------------------ |:--------------------------------------:|
| 00002a37-0000-1000-8000-00805f9b34fb | HEART_RATE_MEASUREMENT                 |
| 00002902-0000-1000-8000-00805f9b34fb | CLIENT_CHARACTERISTIC_CONFIG           |
| 00001800-0000-1000-8000-00805f9b34fb | Generic Access                         |
| 00001801-0000-1000-8000-00805f9b34fb | Generic Attribute                      |
| 0000180d-0000-1000-8000-00805f9b34fb | Heart Rate Service                     |
| 0000180a-0000-1000-8000-00805f9b34fb | Device Information Service             |
| 00002a00-0000-1000-8000-00805f9b34fb | Device Name                            |
| 00002a01-0000-1000-8000-00805f9b34fb | Appearance                             |
| 00002a02-0000-1000-8000-00805f9b34fb | Peripheral Privacy Flag                |
| 00002a03-0000-1000-8000-00805f9b34fb | Reconnection Address                   |
| 00002a04-0000-1000-8000-00805f9b34fb | Peripheral Pref Connection Parameters  |
| 00002a05-0000-1000-8000-00805f9b34fb | Service Changed                        |     
| 00002a23-0000-1000-8000-00805f9b34fb | System ID                              |
| 00002a24-0000-1000-8000-00805f9b34fb | Model Number String                    |
| 00002a25-0000-1000-8000-00805f9b34fb | Serial Number String                   |
| 00002a26-0000-1000-8000-00805f9b34fb | Firmware Revision String               |
| 00002a27-0000-1000-8000-00805f9b34fb | Hardware Revision String               |
| 00002a28-0000-1000-8000-00805f9b34fb | Software Revision String               |
| 00002a29-0000-1000-8000-00805f9b34fb | Manufacturer Name String               | 
| 00002a2a-0000-1000-8000-00805f9b34fb | IEEE 11073-20601 Regulatory Cert List  |
| 00002a50-0000-1000-8000-00805f9b34fb | PnP ID                                 |
| 0000fff0-0000-1000-8000-00805f9b34fb | Custom Service                         |
| 0000fff1-0000-1000-8000-00805f9b34fb | Custom Service Value 1                 |
| 0000fff2-0000-1000-8000-00805f9b34fb | Custom Service Value 2                 |
| 0000fff3-0000-1000-8000-00805f9b34fb | Custom Service Value 3                 |
| 0000fff4-0000-1000-8000-00805f9b34fb | Custom Service Value 4                 |
| 0000fff5-0000-1000-8000-00805f9b34fb | Custom Service Value 5                 |
