variable "credentials" {
  description = "The path to the service account key file"
  default     = "./keys/my-creds.json"
}

variable "region" {
  description = "The location of the resources to create"
  type        = string
  default     = "europe-central2"
}

variable "project" {
  description = "The project ID to deploy resources to"
  type        = string
  default     = "stalwart-fx-449312-u4"
}

variable "location" {
  description = "The location of the resources to create"
  type        = string
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset to create"
  type        = string
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "The name of the GCS bucket to create"
  type        = string
  default     = "terraform-demo-bucket-1"
}

variable "gcs_storage_class" {
  description = "The storage class of the GCS bucket"
  type        = string
  default     = "STANDARD"
}