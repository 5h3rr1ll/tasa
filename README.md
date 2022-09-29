# tasa

The Amazon Search Assistant

This assisten helps you to search for products in the Amazon store and find the best rated products with no effort.

## Troubleshooting

`“chromedriver” cannot be opened because the developer cannot be verified.` </br>

1. Find where the chromedriver is located.

    ```sh
    which chromedriver
    ```

    The output should be something like this:

    ```sh
    /usr/local/bin/chromedriver
    ```

2. Lift the quarantine for the chromedriver binary

    ```sh
    xattr -d com.apple.quarantine /usr/local/bin/chromedriver
    ```

Soultion Source: <https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/>
