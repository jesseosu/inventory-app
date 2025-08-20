variable "region" {
default = "us-east-1"
}


variable "ami" {
description = "Amazon Linux AMI ID"
default = "ami-0c02fb55956c7d316" # Change based on your region
}


variable "instance_type" {
default = "t2.micro"
}


variable "db_user" {
default = "admin"
}


variable "db_password" {
default = "password123"
}


variable "db_name" {
default = "inventory"
}