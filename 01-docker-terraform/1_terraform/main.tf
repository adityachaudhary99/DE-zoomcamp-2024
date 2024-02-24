terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.17.0"
    }
  }
}

provider "google" {
  credentials = "./keys/my-creds.json"
  project = "dauntless-graph-415307"
  region  = "ASIA-SOUTH2"
}



resource "google_storage_bucket" "demo-bucket" {
  name          = "dauntless-graph-415307-terra-bucket"
  location      = "ASIA-SOUTH2"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}