variable "project" {
  description = "Project ID"
  default     = "dauntless-graph-415307"
}

variable "location" {
  description = "Project Location"
  default     = "ASIA-SOUTH2"
}

variable "region" {
  description = "Region"
  default     = "ASIA-SOUTH2"
}

variable "bq_dataset_name" {
  description = "My big query dataset name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My storage bucket name"
  default     = "dauntless-graph-415307-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}

variable "credentials" {
  description = "My credentials"
  default     = "./keys/my-creds.json"
}
