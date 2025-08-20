provider "aws" {
region = var.region
}


resource "aws_instance" "web" {
ami = var.ami
instance_type = var.instance_type
count = 2


user_data = file("../app/user_data.sh")


tags = {
Name = "FlaskWebServer"
}
}


resource "aws_db_instance" "default" {
identifier = "inventory-db"
engine = "mysql"
instance_class = "db.t3.micro"
allocated_storage = 20
username = var.db_user
password = var.db_password
db_name = var.db_name
skip_final_snapshot = true
}