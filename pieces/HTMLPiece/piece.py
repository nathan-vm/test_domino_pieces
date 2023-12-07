from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import base64
class HTMLPiece(BasePiece):
    
    def piece_function(self, input_data: InputModel ):

        self.logger.info("Starting html_content process...")
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Storage Information</title>
        </head>
        <body>

        <div id="storageInfo"></div>

        <script>
            // Function to get information about cookies, session storage, local storage, and indexedDB
            function getStorageInfo() {
                const storageInfo = [];

                // Cookies
                const cookies = document.cookie;
                storageInfo.push({ type: 'Cookies', data: cookies });

                // Session Storage
                const sessionStorageData = JSON.stringify(sessionStorage);
                storageInfo.push({ type: 'Session Storage', data: sessionStorageData });

                // Local Storage
                const localStorageData = JSON.stringify(localStorage);
                storageInfo.push({ type: 'Local Storage', data: localStorageData });

                // IndexedDB
                if ('indexedDB' in window) {
                    const request = window.indexedDB.open('StorageInfoDB', 1);

                    request.onsuccess = function (event) {
                        const db = event.target.result;
                        const transaction = db.transaction(['StorageInfoStore'], 'readonly');
                        const objectStore = transaction.objectStore('StorageInfoStore');
                        const request = objectStore.getAll();

                        request.onsuccess = function (event) {
                            const indexedDBData = JSON.stringify(event.target.result);
                            storageInfo.push({ type: 'IndexedDB', data: indexedDBData });
                            displayStorageInfo(storageInfo);
                        };
                    };
                } else {
                    displayStorageInfo(storageInfo);
                }
            }

            // Function to display storage information in the div and log to console
            function displayStorageInfo(info) {
                const storageInfoDiv = document.getElementById('storageInfo');
                storageInfoDiv.textContent = JSON.stringify(info, null, 2);

                // Log to console
                console.log(info);
            }

            // Call the function to get storage information
            getStorageInfo();
        </script>

        </body>
        </html>
        """

        base64_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')

        self.display_result = {
            "file_type": "html",
            "base64_content": base64_html
        }


        return OutputModel(
            html=html_content,
        )