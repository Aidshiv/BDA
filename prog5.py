$ sudo dnf install -y mongodb mongodb-server


$ sudo systemctl start mongod


$ sudo systemctl enable mongod


$ sudo systemctl status mongod


$ sudo dnf install mongodb-mongosh


$ mongosh


$ use testDB


db.createCollection('Students');


db.students.insertOne({ "_id": 1, "name": "Alice", "age": 22, "marks": 85 })


$ db.students.count({ age: { $gt: 20 } })


$ db.students.find().sort({ age: -1 })


$ db.students.find().sort({ marks: -1 }).limit(3)


$ db.students.find().sort({ marks: -1 }).skip(2)


$ db.students.aggregate([ { $group: { _id: "$age", avgMarks: { $avg: "$marks" } } } ])
