# <p align="center">HolbertonBnB - AirBnB Clone</p>
     
## <p align="center">The console</p>
  
The AirBnb Clone will be our first full web application. The console project is the first step of the building process as shown in the following diagram.



![Image](https://cdn.discordapp.com/attachments/1107668000540209152/1170007483885031464/815046647d23428a14ca.png?ex=65577961&is=65450461&hm=ccd536dbf808563a35e5e34d14599fc917cd6acb54c90d7fa3ea3456832a69b7&)

We'll see the next notion from the projetc in the next weeks.

## Console Settings

#### First step : Clone the repo and open it on your device

```bash
git clone https://github.com/CassandraB670/holbertonschool-AirBnB_clone.git

cd holbertonschool-AirBnb_clone
```

#### Second step : Use the command interpreter

```bash
./console.py
```

#### Third step : The prompt of the console should appear

```bash
(hbtn)
```

#### Fourth step : You can use the console

## Commands

If you enter `help` in the console, all the available commands will be displayed, like this :

```bash
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

| Commands | Function | Usage |
| -------- | -------- | -------- |
| all   | Print the string representation of all instances of given class    | `all <class_name`    |
| count    | Count the number of instances of a given class    | `count <class_name>`    |
| create    | Create a new instance of a given class, print ID and save it into a JSON file    | `create <class_name>`    |
| destroy   |  Deletes a class instance based on its identifier   | `destroy <class_name> <id>`    |
| EOF   | Exit the console by EOF    | -    |
| help    | Displays all the command or give info for one command    | `help <command>`   |
| quit    | Quit the console   | `quit`    |
| show   | Print the string representation of a class instance based on its identifier    | `show <class_name> <id>`    |
| update    | Update a class instance base on its identifier with a given key/value attribute pair or dictionary of attribute pair    | `update <class_name> <id> <attribute_name> "<attribute value>"`    |

## Outputs

#### create :

Command `create`:
```bash
(hbnb) create BaseModel
```
Output:
```bash
49faff9a-6318-451f-87b6-910505c55907
```

Command `all`:
```bash
(hbnb) all MyModel
```
Output:
```bash
** class doesn't exist **
```

Command `show`:
```bash
(hbnb) show BaseModel
```
Output:
```bash
** instance id missing **
```

Command `destroy`:
```bash
(hbnb) destroy
```
Output:
```bash
** class name missing **
```

Command `update` and `show`:
```bash
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
```
Output:
```bash
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

Command `count`:
```bash
(hbnb) count User
```
Output:
```bash
2
```

## Classes

HolbertonBnB utilizes the following classes:

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |
| | | | | | | | | |

## Testing

Unittests for the HolbertonBnB project are defined in the tests folder
. To run the test files :

```
$ python3 -m unittest -v tests.test_models.test_amenity
$ python3 -m unittest -v tests.test_models.test_base_model
$ python3 -m unittest -v tests.test_models.test_city
$ python3 -m unittest -v tests.test_models.test_place
...
$ python3 -m unittest -v tests.test_models.test_engine.test_file_storage
```


## Authors

Cassandra BOUDIER https://github.com/CassandraB670

Christophe BOUDIER https://github.com/BIDcolonel

## License

« Copyright © <BOUDIER Cassandra and BOUDIER Christophe - 2023 November >

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The Software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the Software. »
