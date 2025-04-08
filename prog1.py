# Create a local directory named Hadoop
$ mkdir Hadoop

# Change to the Hadoop directory
$ cd Hadoop/

# Create a file named hello.txt and open it in the vi editor
$ vi hello.txt

# Display the content of the hello.txt file
$ cat hello.txt

# Create a directory in HDFS named today
$ hdfs dfs -mkdir /today

# Copy the hello.txt file from the local Hadoop directory to HDFS, renaming it to data.txt
$ hdfs dfs -put hello.txt /today/data.txt

# Create another directory in HDFS named input
$ hdfs dfs -mkdir /input

# Copy the data.txt file within HDFS from /today to /input
$ hdfs dfs -cp /today/data.txt /input/data.txt

# Display the content of the copied file in HDFS
$ hdfs dfs -cat /input/data.txt

# Copy the data.txt file from HDFS back to the local Hadoop directory
$ hdfs dfs -get /input/data.txt

# Delete the data.txt file from HDFS
$ hdfs dfs -rm /today/data.txt

# Remove the /today directory from HDFS
$ hdfs dfs -rmdir /today
