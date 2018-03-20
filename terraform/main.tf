# The following table shows the schema required by libfaketimefs-ctl.

resource "random_id" "name" {
  byte_length = 4
  prefix      = "libfaketimefs-ctl-"
}

resource "aws_dynamodb_table" "libfaketimefs" {
  name           = "${random_id.name.hex}"
  read_capacity  = 1
  write_capacity = 1

  hash_key = "Id"

  attribute {
    name = "Id"
    type = "S"
  }
}

output "table" {
  value = "${random_id.name.hex}"
}
