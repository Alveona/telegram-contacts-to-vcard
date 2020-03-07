## Export your Telegram contacts to vCard format and import it to your phone


### Export your Telegram data

In Telegram Desktop go to Settings - Advanced - Export your Telegram data   
*If you're on Mac OS and don't have Advanced option in your client, try Telegram Lite from Mac App Store*  
Choose only 'Contacts' option  
In the very bottom of the window there will be an option 'Machine-readable JSON', choose it.  

You will receive a `results.json` file that will be very simillar to 'example.json' in this repo  
Rename it to `example.json` or choose `FILE_NAME_IN` constant in `main.py`  

### Usage

    git clone https://github.com/Alveona/telegram-contacts-to-vcard.git
    cd telegram-contacts-to-vcard
    python -m pip install -r requirements.txt
    python main.py

The output will be in `example.vcf` if you didn't change `FILE_NAME_OUT` constant
