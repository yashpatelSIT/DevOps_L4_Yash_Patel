terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "my_example_file" {
  filename = "${path.module}/example.txt"
  content  = "Hello from updated Terraform!"
}