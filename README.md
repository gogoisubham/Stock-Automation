# Stock Automation Project

## Overview

The **Stock Automation Project** is a Python-based automation script that retrieves stock data for a specified ticker symbol, processes the data, and sends a daily summary email to a recipient. The project is designed to run automatically using a cron job, allowing users to receive up-to-date stock information without manual intervention.

## Features

- **Automated Stock Data Retrieval:** The script automatically downloads stock data for a specified ticker (e.g., AAPL).
- **Data Processing:** The downloaded data is processed to provide summary statistics.
- **Daily Email Summary:** A daily email is sent to a specified recipient with the processed stock data summary.
- **Cron Job Automation:** The automation is handled via a cron job, which is configured in `cronjob.txt`.
- **Logging:** The execution of the cron jobs is logged in `cronjob.log`.

## Project Structure

```plaintext
Stock-automation/
├── cronjob.log           # Log file that records the outputs of cron jobs
├── cronjob.txt           # File containing the cron job configuration
├── stock_automation.py   # Main Python script for automating stock data retrieval and email sending
└── README.md             # Project documentation
```

## File Descriptions

- **cronjob.log**: This file contains the logged information for all the cron jobs that have run or will be running in the future. It records the success or failure of the script execution, along with any relevant output or errors.
- **cronjob.txt**: This file contains the configuration of the cron job that automates the execution of the stock_automation.py script. It details the schedule and command used to trigger the script.
- **stock_automation.py**: The main Python script that handles the entire automation process. It downloads stock data, processes it to generate summary statistics, and sends an email containing the summary.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- Git
- Cron (Linux/macOS) or Task Scheduler (Windows) if you plan to set up the cron job manually.

### Installation

1.	Clone the repository:
    ```bash
    git clone https://github.com/your-username/Stock-Automation.git
    cd Stock-automation
    ```
2.	Set up environment variables:
Ensure your environment variables for the email credentials are correctly set up. You can export them in your shell or include them in the cron job:
    ```plaintext
    export MAIL_USERNAME='your-email@example.com'
    export MAIL_PASSWORD='your-email-password'
    ```
3. Set up the cron job:
The cron job is configured to automate the execution of the script. The configuration is stored in cronjob.txt. To apply this cron job configuration:
    ```bash
    crontab cronjob.txt
    ```

This will set up the cron job according to the schedule defined in the cronjob.txt file.

## Usage

1.	Run the script manually (optional):
    You can run the script manually to ensure it works correctly:
    ```bash
    python3 stock_automation.py
    ```

    This will download the stock data, process it, and send an email with the summary.

2.	Check the log file:
The cronjob.log file will capture all the output from the cron jobs, including any errors. You can monitor this file to ensure that the cron jobs are running as expected:
    ```terminal
    cat cronjob.log
    ```

### Customization

You can customize the following in the stock_automation.py script:

- **Ticker Symbol**: Modify the ticker variable to track a different stock.
- **Email Recipient**: Update the recipient variable to send the summary to a different email address.

### Known Issues

- Ensure that the Python script has the correct permissions to run in the environment where the cron job is set up.
- The cronjob.log file may grow large over time. Consider setting up log rotation or periodically clearing the log file.

### Future Improvements

- Implement additional error handling and notification if the script fails.
- Add support for tracking multiple stock tickers.
- Enhance the logging mechanism to include more detailed information about each execution.

### Contributing

Contributions are welcome! Please fork the repository and create a pull request to propose changes or improvements.

### Author

- **Subham Gogoi** - https://github.com/gogoisubham

For any questions or suggestions, please reach out to subhgogoi@gmail.com