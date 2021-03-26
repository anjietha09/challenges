resource "aws_s3_bucket" "terraform_state_s3_bucket" {
    bucket = var.bucket_name
 
    versioning {
      enabled = true
    }
 
    lifecycle {
      prevent_destroy = true
    }
 
    tags {
      Group= var.name
    }      
}

resource "aws_dynamodb_table" "terraform_state_locking_dynamodb" {
  name = var.dynamodb_name
  hash_key = "LockID"
  read_capacity = 20
  write_capacity = 20
 
  attribute {
    name = "LockID"
    type = "S"
  }
 
  tags {
    Group = var.name
  }
}