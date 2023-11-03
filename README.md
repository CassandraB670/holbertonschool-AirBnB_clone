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