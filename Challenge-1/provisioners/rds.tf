resource "aws_security_group" "rds" {
  name = "${format("%s-rds-sg", var.name)}"

  vpc_id = module.vpc.vpc_id

  ingress {
    from_port   = var.db_port
    to_port     = var.db_port
    protocol    = "tcp"
    cidr_blocks = [module.vpc.private_subnets_cidr_blocks]
  }

  tags {
    Group = var.name
  }

}

module "rds" {
  source = "terraform-aws-modules/rds/aws"

  identifier = var.db_identifier

  engine            = "postgres"
  engine_version    = "9.6.3"
  instance_class    = "db.t2.micro"
  allocated_storage = var.db_allocated_storage

  name = var.db_name
  username = var.db_username
  password = var.db_password
  port     = var.db_port

  vpc_security_group_ids = [aws_security_group.rds.id]

  maintenance_window = var.db_maintenance_window
  backup_window      = var.db_backup_window

  # disable backups to create DB faster
  backup_retention_period = var.db_backup_retention_period

  subnet_ids = [module.vpc.database_subnets]

  family = "postgres9.6"

  tags {
    Group = var.name
  }

}