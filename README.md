# Employee Monitoring Python Based application

This is a Python-based desktop agent designed to track employee activity and upload screenshots and logs to AWS S3 or a similar cloud storage service. The application runs in the background, capturing user activity and ensuring robust error handling and security practices.

## Features

- **Activity Tracking**:
  - Monitors user inputs (mouse and keyboard) to differentiate between genuine and scripted activity.
  - Can capture screenshots at configurable intervals.
  
- **Configurable Screenshots**:
  - Option to capture blurred or unblurred screenshots.
  - Screenshot intervals are configurable (e.g., every 5 minutes, 10 minutes, etc.).
  
- **Real-time Configuration Updates**:
  - The agent polls for configuration updates from a web application and applies changes instantly.
  
- **Time Zone Management**:
  - Automatically adjusts for any time zone changes and reflects them in activity logs.
  
- **Data Upload**:
  - Uploads captured screenshots and logs to AWS S3 using secure encryption.
  - Handles large file uploads efficiently, with compression and chunked uploads.
  
- **Error Handling**:
  - Resilient against network disconnections, firewall restrictions, and abrupt application shutdowns.
  
- **Single Instance Management**:
  - Ensures only one instance of the application is running at a time.

## Requirements

- **Python 3.x**
- **AWS credentials** (for S3 integration)
- Libraries listed in `requirements.txt`

## Installation

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/employee-monitoring-app.git
cd employee-monitoring-app
