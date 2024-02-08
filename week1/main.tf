terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.34.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = "us-east-1"
}

resource "aws_s3_bucket" "terra-demo" {
  bucket = "terra-demo-bucket"
  acl    = "private"

  versioning {
    enabled = true
  }

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
