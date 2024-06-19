# Slack-Bot


# Earthquake Notification Script

This script fetches the latest earthquake data from the AFAD website and sends details of the most recent earthquake with a magnitude greater than 2 to a specified Slack channel.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `python-dotenv` library
- A Slack token with permission to post messages to a channel

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/earthquake-notification-script.git
    cd earthquake-notification-script
    ```

2. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4 python-dotenv
    ```

3. Create a `.env` file in the project directory and add your Slack token:
    ```env
    SLACK_TOKEN=your-slack-token-here
    ```

## Usage

Run the script to fetch the latest earthquake data and send a notification to Slack:
```sh
python earthquake_notification.py
```

## Script Details

### `fetch_latest_earthquake()`

This function fetches the latest earthquake data from the AFAD website. It parses the HTML to find the most recent earthquake with a magnitude greater than 2 and returns the formatted details.

### `send_to_slack(message)`

This function sends a given message to the specified Slack channel using the Slack Web API.

## Example

1. Fetching the latest earthquake data:
    ```python
    result = fetch_latest_earthquake()
    ```

2. Sending the fetched data to Slack:
    ```python
    if result:
        send_to_slack(result)
    else:
        send_to_slack("No data available")
    ```

## License

This project is licensed under the MIT License.
