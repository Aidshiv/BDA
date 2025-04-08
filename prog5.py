
$sudo dnf install -y mongodb mongodb-server
$sudo systemctl start mongod
$sudo systemctl enable mongod
$sudo systemctl status mongod
$sudo dnf install mongodb-mongosh
Start the MongoDB shell by running:
$mangosh
Select a database
$use testDB
Sample Data:
[
 { "_id": 1, "name": "Alice", "age": 22, "marks": 85 },
 { "_id": 2, "name": "Bob", "age": 21, "marks": 78 },
 { "_id": 3, "name": "Charlie", "age": 23, "marks": 92 },
 { "_id": 4, "name": "David", "age": 20, "marks": 88 },
 { "_id": 5, "name": "Eve", "age": 22, "marks": 76 }
]
Create students collection using above sample data
db.createCollection('Students');
db.student.insertOne({ "_id": 1, "name": "Alice", "age": 22, "marks": 85 })

$ use testDB


db.createCollection('Students');


db.students.insertOne({ "_id": 1, "name": "Alice", "age": 22, "marks": 85 })


$ db.students.count({ age: { $gt: 20 } })


$ db.students.find().sort({ age: -1 })


$ db.students.find().sort({ marks: -1 }).limit(3)


$ db.students.find().sort({ marks: -1 }).skip(2)


$ db.students.aggregate([ { $group: { _id: "$age", avgMarks: { $avg: "$marks" } } } ])
