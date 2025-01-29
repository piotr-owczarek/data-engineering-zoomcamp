terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  project = "stalwart-fx-449312-u4"
  region  = "europe-central2"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-demo-bucket-1"
  location      = "EU"
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