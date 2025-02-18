resource "google_cloud_scheduler_job" "clean_assistant" {
  name      = "clean-assistant"
  region    = var.region
  schedule  = "0 10 * * *"
  time_zone = "Asia/Tokyo"

  http_target {
    uri         = "https://${var.region}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${var.project_id}/jobs/${google_cloud_run_v2_job.clean_assistant.name}:run"
    http_method = "POST"

    oauth_token {
      service_account_email = google_service_account.cloud_scheduler_sa.email
    }
  }

  depends_on = [
    google_project_service.cloud_scheduler
  ]
}
