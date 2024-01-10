// js/scanner.js

document.addEventListener("DOMContentLoaded", function () {
    const apiUrl = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=AIzaSyCwyiJXhkQv0zCP5wmVUQVJ4dD0gPqA3KU"; // Replace with your Google Safe Browsing API key
  
    const scanButton = document.getElementById("scanButton");
    const urlInput = document.getElementById("urlInput");
    const resultContainer = document.getElementById("resultContainer");
  
    scanButton.addEventListener("click", function () {
      const urlToScan = urlInput.value.trim();
  
      if (urlToScan === "") {
        alert("Please enter a URL to scan.");
        return;
      }
  
      // Make API request to Google Safe Browsing API
      fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          client: {
            clientId: "your-client-id", // Replace with your client ID
            clientVersion: "1.0",
          },
          threatInfo: {
            threatTypes: ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
            platformTypes: ["ANY_PLATFORM"],
            threatEntryTypes: ["URL"],
            threatEntries: [{ url: urlToScan }],
          },
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          // Process the scan results and update the UI
          displayResults(data);
        })
        .catch((error) => {
          console.error("Error scanning URL:", error);
        });
    });
  
    function displayResults(results) {
      // Implement the logic to display scan results on results.html
      // You can customize this based on your UI requirements
      // For example, update the resultContainer.innerHTML with the results
    }
  });
  